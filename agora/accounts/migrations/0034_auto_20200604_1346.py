# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-06-04 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_auto_20200529_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='epp_bai_0_id',
            field=models.CharField(default='-', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organisation',
            name='epp_bai_1_name',
            field=models.CharField(default='-', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
