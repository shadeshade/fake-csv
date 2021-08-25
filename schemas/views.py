import os

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db import transaction, IntegrityError
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .forms import SchemaForm, ColumnUpdateFormSet, ColumnCreateFormSet, JobCreateForm
from .models import Schema, Column, Job
from .tools import start_job, parse_column_form_data


class SchemaListView(LoginRequiredMixin, ListView):
    model = Schema
    template_name = 'schemas/schema_list.html'
    paginate_by = 15
    ordering = '-pk'

    def get_queryset(self):
        self.queryset = super().get_queryset().filter(added_by=self.request.user)
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.queryset
        return context


class SchemaCreateView(LoginRequiredMixin, CreateView):
    template_name = 'schemas/schema_create.html'

    def get_context_data(self, **kwargs):
        kwargs['schema_form'] = SchemaForm()
        kwargs['column_form'] = ColumnCreateFormSet(queryset=Column.objects.none())
        return kwargs

    def post(self, request, *args, **kwargs):
        schema_form = SchemaForm(request.POST)
        column_form = ColumnCreateFormSet(parse_column_form_data(request.POST))

        try:
           if len(column_form) == 0:
               raise Exception
        except Exception:
            messages.error(request, 'Columns should be provided')
        else:
            if schema_form.is_valid() and column_form.is_valid():  # Check if submitted forms are valid
                try:
                    with transaction.atomic():
                        schema = schema_form.save(commit=False)
                        schema.added_by = request.user
                        schema.save()

                        for form in column_form:
                            column = form.save(commit=False)
                            column.schema = schema
                            column.save()

                    return redirect(reverse_lazy('schemas:schema_list'))

                except IntegrityError:
                    messages.error(request, 'Database error encountered')

        context = {
            'schema_form': schema_form,
            'column_form': column_form,
        }
        return render(request, template_name=self.template_name, context=context)


class SchemaDetailView(DetailView):
    model = Schema
    template_name = 'schemas/schema_detail.html'


class SchemaUpdateView(UserPassesTestMixin, UpdateView):
    model = Schema
    template_name = 'schemas/schema_update.html'
    fields = ['name', 'column_separator', 'string_character', ]

    def get_context_data(self, **kwargs):
        kwargs['schema_form'] = SchemaForm(instance=self.object)
        kwargs['column_form'] = ColumnUpdateFormSet(queryset=Column.objects.filter(schema=self.object))
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        schema_form = SchemaForm(instance=self.object, data=request.POST)
        column_form = ColumnUpdateFormSet(parse_column_form_data(request.POST))

        try:
            if len(column_form) == 0:
                raise Exception
        except Exception:
            messages.error(request, 'Columns should be provided')
        else:
            if schema_form.is_valid() and column_form.is_valid():  # Check if submitted forms are valid
                try:
                    with transaction.atomic():
                        schema_form.save()
                        # delete all columns related to the schema and add new columns
                        Column.objects.filter(schema=self.object).delete()

                        for form in column_form:
                            column = form.save(commit=False)
                            column.schema = self.object
                            column.save()
                    return redirect(reverse_lazy('schemas:schema_list'))

                except IntegrityError:
                    messages.error(request, 'Database error encountered')

        context = {
            'schema_form': schema_form,
            'column_form': column_form,
        }
        return render(request, template_name=self.template_name, context=context)

    def test_func(self):
        schema = self.get_object()
        user = self.request.user
        return schema.added_by == user or user.is_staff


class SchemaDeleteView(UserPassesTestMixin, DeleteView):
    model = Schema
    template_name = 'schemas/delete_confirm.html'
    success_url = reverse_lazy('schemas:schema_list')

    def test_func(self):
        schema = self.get_object()
        user = self.request.user
        return schema.added_by == user or user.is_staff


class DatasetView(UserPassesTestMixin, CreateView, ListView):
    model = Job
    template_name = 'schemas/data_sets.html'
    fields = []

    def get_queryset(self):
        self.queryset = super().get_queryset().filter(payload__schema_id=self.kwargs['schema_pk'])
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['row_form'] = JobCreateForm  # add form to specify number of rows
        return context

    def post(self, request, *args, **kwargs):
        form = JobCreateForm(request.POST)
        if form.is_valid():
            start_job(schema_id=kwargs['schema_pk'], rows_count=form.cleaned_data['rows'])

        return redirect(reverse_lazy('schemas:data_set', kwargs={'schema_pk': kwargs['schema_pk']}))

    def test_func(self):
        schema = Schema.objects.get(pk=self.kwargs['schema_pk'])
        user = self.request.user
        return schema.added_by == user or user.is_staff


class DownloadView(UserPassesTestMixin, View):
    def get(self, request,  *args, **kwargs):
        file_name = f"fake-schema-{self.kwargs['job_pk']}.csv"
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        raise Http404

    def test_func(self):
        job = Job.objects.get(pk=self.kwargs['job_pk'])
        schema = Schema.objects.get(pk=job.payload["schema_id"])
        user = self.request.user
        return schema.added_by == user or user.is_staff



