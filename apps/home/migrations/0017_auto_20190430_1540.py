# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-30 15:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_delete_webstudy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialmode',
            options={'ordering': ['id'], 'verbose_name': '社交', 'verbose_name_plural': '社交'},
        ),
    ]
