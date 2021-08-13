from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Schema
from .forms import SchemaCreateForm, ColumnCreateForm


class SchemaListView(ListView):
    model = Schema
    template_name = 'schemas/schema_list.html'
    paginate_by = 25


class SchemaCreateView(CreateView):
    model = Schema
    template_name = 'schemas/schema_create.html'
    success_url = reverse_lazy('schemas:schemas_list')

    def get_context_data(self, **kwargs):
        kwargs['schema_form'] = SchemaCreateForm()
        kwargs['column_form'] = ColumnCreateForm()
        return kwargs
