# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-23 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190423_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homewelcome',
            name='pic1_path',
            field=models.FileField(default='/static/images/default.png', upload_to='welcome', verbose_name='图片1路径'),
        ),
        migrations.AlterField(
            model_name='homewelcome',
            name='pic2_path',
            field=models.FileField(default='/static/images/default.png', upload_to='welcome', verbose_name='图片2路径'),
        ),
    ]
