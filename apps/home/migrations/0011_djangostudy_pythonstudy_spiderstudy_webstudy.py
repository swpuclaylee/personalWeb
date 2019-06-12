# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-23 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190423_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50, verbose_name='Django学习')),
                ('sourceUrl', models.URLField(max_length=50, verbose_name='Django学习连接')),
            ],
            options={
                'verbose_name': '学习Django',
                'verbose_name_plural': '学习Django',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PythonStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50, verbose_name='python学习')),
                ('sourceUrl', models.URLField(max_length=50, verbose_name='python学习连接')),
            ],
            options={
                'verbose_name': '学习Python',
                'verbose_name_plural': '学习Python',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SpiderStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50, verbose_name='Spider学习')),
                ('sourceUrl', models.URLField(max_length=50, verbose_name='Spider学习连接')),
            ],
            options={
                'verbose_name': '学习Spider',
                'verbose_name_plural': '学习Spider',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WebStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50, verbose_name='Web学习')),
                ('sourceUrl', models.URLField(max_length=50, verbose_name='Web学习连接')),
            ],
            options={
                'verbose_name': '学习Web',
                'verbose_name_plural': '学习Web',
                'ordering': ['id'],
            },
        ),
    ]
