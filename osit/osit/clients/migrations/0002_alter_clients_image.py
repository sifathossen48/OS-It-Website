# Generated by Django 5.0.1 on 2024-02-05 06:04

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[300, 300], upload_to='client_images/'),
        ),
    ]
