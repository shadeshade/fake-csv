# Generated by Django 3.2.6 on 2021-08-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0004_auto_20210825_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
