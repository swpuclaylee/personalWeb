# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-17 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_category_app'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='app',
        ),
    ]