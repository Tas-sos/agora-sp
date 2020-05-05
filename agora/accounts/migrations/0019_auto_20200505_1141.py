# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-05-05 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20200504_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='pd_mti_1_life_cycle_status',
            field=models.CharField(blank=True, choices=[['Under Construction', 'Under Construction'], ['Operational', 'Operational'], ['Being Upgraded', 'Being Upgraded'], ['Other', 'Other']], default=None, max_length=255, null=True, verbose_name=b'PD.MTI.1_Life_Cycle_Status'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='pd_mti_2_certifications',
            field=models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name=b'PD.MTI.2_Certifications'),
        ),
    ]
