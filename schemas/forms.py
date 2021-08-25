from django import forms

from . import choices
from .models import Schema, Column


class SchemaForm(forms.ModelForm):

    class Meta:
        model = Schema

        fields = [
            'name',
            'column_separator',
            'string_character',
        ]


class ColumnForm(forms.ModelForm):

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

    def clean_type(self):
        type_ = self.cleaned_data.get('type')

        if not self.cleaned_data.get('type'):
            raise forms.ValidationError("Type field is required")
        return type_

    def clean_quantity(self):
        type_ = self.cleaned_data.get('type')

        if type_ == choices.TEXT:
            quantity = self.cleaned_data.get('quantity')
            if not quantity:
                raise forms.ValidationError("Quantity field is required")

            return quantity

    def clean_range_from(self):
        type_ = self.cleaned_data.get('type')

        if type_ == choices.INT:
            range_from = self.cleaned_data.get('range_from')

            if not range_from:
                raise forms.ValidationError("All range fields are required")
            elif range_from < 0:
                raise forms.ValidationError("Range from field should be greater than or equal to zero")

            return range_from

    def clean_range_to(self):
        type_ = self.cleaned_data.get('type')

        if type_ == choices.INT:
            range_from = self.cleaned_data.get('range_from')
            range_to = self.cleaned_data.get('range_to')

            if not range_to:
                raise forms.ValidationError("All range fields are required")
            elif range_from > range_to:
                raise forms.ValidationError("Invalid range")

            return range_to


class JobCreateForm(forms.Form):

    rows = forms.IntegerField(label='Rows', error_messages={'required': 'This field is required'})

    def clean_rows(self):
        data = self.cleaned_data['rows']
        if not data > 0:
            raise forms.ValidationError("Should be greater then 0")

        return data


# we want to have 1 extra row to make it easier to create schemas
ColumnCreateFormSet = forms.modelformset_factory(Column, ColumnForm, extra=1)
# we want to have 0 extra row for update page
ColumnUpdateFormSet = forms.modelformset_factory(Column, ColumnForm, extra=0)
