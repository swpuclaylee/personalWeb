# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-17 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0003_auto_20190516_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstBookModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bClassFirst', models.CharField(blank=True, max_length=50, null=True)),
                ('bClassSecond', models.CharField(blank=True, max_length=50, null=True)),
                ('bName', models.CharField(blank=True, max_length=50, null=True, verbose_name='书名')),
                ('bImage', models.ImageField(default='', upload_to='book/', verbose_name='图片路径')),
                ('bComment', models.CharField(blank=True, max_length=5000, null=True, verbose_name='书籍评价')),
                ('bAuthor', models.CharField(blank=True, max_length=50, null=True, verbose_name='书籍作者')),
                ('bUrl', models.URLField(blank=True, max_length=100, null=True, verbose_name='书籍连接')),
            ],
            options={
                'verbose_name': '书籍推荐',
                'verbose_name_plural': '书籍推荐',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SecondBookModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bName', models.CharField(blank=True, max_length=50, null=True, verbose_name='书名')),
                ('bImage', models.ImageField(default='', upload_to='book/', verbose_name='图片路径')),
                ('bComment', models.CharField(blank=True, max_length=5000, null=True, verbose_name='书籍评价')),
                ('bAuthor', models.CharField(blank=True, max_length=50, null=True, verbose_name='书籍作者')),
                ('bUrl', models.URLField(blank=True, max_length=100, null=True, verbose_name='书籍连接')),
            ],
            options={
                'verbose_name': '书籍推荐',
                'verbose_name_plural': '书籍推荐',
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='BookModel',
        ),
    ]
