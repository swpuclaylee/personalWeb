# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-23 17:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_djangostudy_pythonstudy_spiderstudy_webstudy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DjangoStudy',
        ),
        migrations.DeleteModel(
            name='PythonStudy',
        ),
        migrations.DeleteModel(
            name='SpiderStudy',
        ),
        migrations.DeleteModel(
            name='WebStudy',
        ),
    ]
