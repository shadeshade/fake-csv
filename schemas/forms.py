from django.forms import ModelForm, formset_factory
from .models import Schema, Column


class SchemaCreateForm(ModelForm):
    class Meta:
        model = Schema

        fields = [
            'name',
            'column_separator',
            'string_character',
        ]


class ColumnCreateForm(ModelForm):
    class Meta:
        model = Column

        fields = [
            'column_name',
            'type',
            'range_from',
            'range_to',
            'quantity',
            'order',
        ]


ColumnCreateFormSet = formset_factory(ColumnCreateForm, max_num=9)
