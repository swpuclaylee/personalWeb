# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-28 17:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_socialmode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialmode',
            options={'verbose_name': '社交', 'verbose_name_plural': '社交'},
        ),
    ]