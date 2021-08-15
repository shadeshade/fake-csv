from django.db import transaction, IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView

from .forms import SchemaCreateForm, ColumnCreateFormSet
from .models import Schema


class SchemaListView(ListView):
    model = Schema
    template_name = 'schemas/schema_list.html'
    paginate_by = 25


class SchemaCreateView(TemplateView):
    template_name = 'schemas/schema_create.html'

    def get_context_data(self, **kwargs):
        kwargs['schema_form'] = SchemaCreateForm()
        kwargs['column_form'] = ColumnCreateFormSet()
        return kwargs

    def post(self, request, *args, **kwargs):
        schema_form = SchemaCreateForm(request.POST)
        column_form = ColumnCreateFormSet(request.POST)

        if schema_form.is_valid() and column_form.is_valid():
            try:
                with transaction.atomic():
                    schema = schema_form.save(commit=False)
                    schema.added_by = request.user
                    schema.save()

                    for column in column_form:
                        col = column.save(commit=False)
                        col.schema = schema
                        col.save()
            except IntegrityError:
                print('Error Encountered')
            return redirect(reverse_lazy('schemas:schema_list'))
