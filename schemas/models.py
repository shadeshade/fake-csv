from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone
from . import choices
from .choices import JOB_STATUS


class Schema(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    column_separator = models.CharField(
        max_length=50, choices=choices.SEPARATORS, default=choices.COM)
    string_character = models.CharField(
        max_length=50, choices=choices.QUOTATION_CHARACTERS, default=choices.DBL)
    created = models.DateTimeField(null=False, default=timezone.now, editable=False)
    modified = models.DateTimeField(null=False, default=timezone.now, editable=False)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class Column(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=choices.TYPES)
    range_from = models.PositiveIntegerField(blank=True, null=True)
    range_to = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=False, null=False)
    schema = models.ForeignKey(Schema, related_name='columns', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class Job(models.Model):
    created = models.DateTimeField(null=False, default=timezone.now, editable=False)
    status = models.PositiveSmallIntegerField(choices=JOB_STATUS, default=JOB_STATUS.PROCESSING)
    arguments = models.JSONField()

