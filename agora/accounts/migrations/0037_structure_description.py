# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-06-15 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_esfridomain_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='structure',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
