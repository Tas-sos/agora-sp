# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-25 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_auto_20180104_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicearea',
            name='icon',
            field=models.ImageField(default=b'service-area-icon-default.jpg', upload_to=b''),
        ),
    ]