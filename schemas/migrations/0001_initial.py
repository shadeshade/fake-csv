# Generated by Django 3.2.6 on 2021-08-12 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('column_separator', models.CharField(choices=[('Comma', 'Comma (,)'), ('Semicolon', 'Semicolon (;)'), ('Tab', 'Tab (\\t)'), ('Space', 'Space ( )'), ('Pipe', 'Pipe (|)')], default='Comma', max_length=50)),
                ('string_character', models.CharField(choices=[('Double-quote', 'Double-quote (")'), ('Single-quote', "Single-quote (')")], default='Double-quote', max_length=50)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
