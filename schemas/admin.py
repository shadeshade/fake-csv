from django.contrib import admin
from .models import Schema, Column, Job

admin.site.register(Schema)
admin.site.register(Column)
admin.site.register(Job)
