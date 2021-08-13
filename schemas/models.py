from django.contrib.auth.models import User
from django.db import models

from . import choices


class Schema(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    column_separator = models.CharField(
        max_length=50, choices=choices.SEPARATORS, default=choices.COM)
    string_character = models.CharField(
        max_length=50, choices=choices.QUOTATION_CHARACTERS, default=choices.DBL)


class Column(models.Model):
    column_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=choices.TYPES)
    range_from = models.PositiveIntegerField(blank=True, null=True)
    range_to = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=False, null=False)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
