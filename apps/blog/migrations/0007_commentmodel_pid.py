# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-20 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190520_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='pid',
            field=models.IntegerField(default='0', verbose_name='id'),
        ),
    ]