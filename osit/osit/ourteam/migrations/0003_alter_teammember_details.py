# Generated by Django 5.0.1 on 2024-01-27 19:45

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourteam', '0002_alter_teammember_details_alter_teammember_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='details',
            field=tinymce.models.HTMLField(max_length=4000),
        ),
    ]
