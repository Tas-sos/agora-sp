# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-06-10 15:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0081_auto_20200610_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='erp_cli_5_tags',
            new_name='erp_cli_8_tags',
        ),
    ]