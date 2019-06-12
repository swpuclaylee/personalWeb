# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-19 16:14
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_articlemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='博客内容'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='评论内容'),
        ),
    ]