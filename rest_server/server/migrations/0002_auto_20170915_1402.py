# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmphoto',
            name='photo',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='housephoto',
            name='photo',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='wellphoto',
            name='photo',
            field=models.ImageField(upload_to=b''),
        ),
    ]
