# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0012_auto_20171121_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='crop',
            field=models.CharField(max_length=50),
        ),
    ]
