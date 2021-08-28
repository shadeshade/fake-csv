from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from . import choices
from .choices import JOB_STATUS


class Schema(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    column_separator = models.CharField(
        max_length=50,
        choices=choices.SEPARATORS,
        default=choices.COM
    )
    string_character = models.CharField(
        max_length=50,
        choices=choices.QUOTATION_CHARACTERS,
        default=choices.DBL
    )
    created = models.DateTimeField(null=False, default=timezone.now, editable=False)
    modified = models.DateTimeField(null=False, default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if not self._state.adding:  # update field modified if the model was edited
            self.modified = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class Column(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=choices.TYPES)
    range_from = models.PositiveIntegerField(blank=True, null=True)
    range_to = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField()
    schema = models.ForeignKey(Schema, related_name='columns', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class Job(models.Model):
    created = models.DateTimeField(default=timezone.now, editable=False)
    status = models.CharField(max_length=50, choices=JOB_STATUS, default=choices.PROCESSING)
    error = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=200, null=True)
    payload = models.JSONField(default=dict)

    def __str__(self):
        return f'job: {self.pk}'
