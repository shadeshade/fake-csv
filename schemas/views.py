from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db import transaction, IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .forms import SchemaForm, ColumnUpdateFormSet, ColumnCreateFormSet
from .models import Schema, Column


class SchemaListView(LoginRequiredMixin, ListView):
    model = Schema
    template_name = 'schemas/schema_list.html'
    paginate_by = 15
    ordering = '-pk'

    def get_queryset(self):
        self.queryset = super().get_queryset().filter(added_by=self.request.user)
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # this calls self.get_queryset() which assigns self.form
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
        column_form = ColumnCreateFormSet(request.POST)

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
            except IntegrityError:
                print('Error Encountered')
            return redirect(reverse_lazy('schemas:schema_list'))


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
        column_form = ColumnUpdateFormSet(request.POST)

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
            except IntegrityError:
                print('Error Encountered')
        return redirect(reverse_lazy('schemas:schema_list'))

    def test_func(self):
        schema = self.get_object()
        user = self.request.user
        return schema.added_by == user or user.is_staff


class SchemaDeleteView(UserPassesTestMixin, DeleteView):
    model = Schema
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('schemas:schema_list')

    def test_func(self):
        schema = self.get_object()
        user = self.request.user
        return schema.added_by == user or user.is_staff
