# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-18 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmessagemodel',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='联系人姓名'),
        ),
    ]
