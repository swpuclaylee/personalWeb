# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-15 17:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20190514_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homewelcome',
            name='pic2_path',
        ),
    ]
