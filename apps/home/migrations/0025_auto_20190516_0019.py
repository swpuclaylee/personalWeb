# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-16 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_funnyparagraphmodel_humorousjokemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funnyparagraphmodel',
            name='pContent',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='内容'),
        ),
    ]
