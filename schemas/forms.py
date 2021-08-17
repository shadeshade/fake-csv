from django.forms import ModelForm, modelformset_factory, Form, IntegerField, ChoiceField, Textarea

from .choices import NAME
from .models import Schema, Column


class SchemaForm(ModelForm):
    class Meta:
        model = Schema

        fields = [
            'name',
            'column_separator',
            'string_character',
        ]


class ColumnForm(ModelForm):
    class Meta:
        model = Column

        fields = [
            'name',
            'type',
            'range_from',
            'range_to',
            'quantity',
            'order',
        ]


# we want to have 1 extra row to make it easier to create schemas
ColumnCreateFormSet = modelformset_factory(Column, ColumnForm, extra=1)
# we want to have 0 extra row for update page
ColumnUpdateFormSet = modelformset_factory(Column, ColumnForm, extra=0)
