# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-19 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='image',
            field=models.ImageField(default='', upload_to='blog/'),
        ),
    ]