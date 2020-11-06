# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-05-07 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0060_auto_20200506_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='rd_mgi_1_helpdesk_webpage',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='rd_mgi_2_helpdesk_email',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='rd_mgi_3_user_manual',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='rd_mgi_4_terms_of_use',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='rd_mgi_5_privacy_policy',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='rd_mgi_6_sla_specification',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='rd_mgi_7_training_information',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='rd_mgi_8_status_monitoring',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='rd_mgi_9_maintenance',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]