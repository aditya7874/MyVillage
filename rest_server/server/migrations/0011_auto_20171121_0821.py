# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_market'),
    ]

    operations = [
        migrations.RenameField(
            model_name='market',
            old_name='date',
            new_name='month',
        ),
        migrations.AddField(
            model_name='market',
            name='crop',
            field=models.ForeignKey(default='Onion', on_delete=django.db.models.deletion.CASCADE, to='server.crop'),
        ),
    ]
