# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-15 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_remove_homewelcome_pic2_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunnyParagraphModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pClass', models.CharField(blank=True, max_length=50, null=True, verbose_name='类')),
                ('pId', models.CharField(blank=True, max_length=50, null=True, verbose_name='id')),
                ('pImage', models.ImageField(default='', upload_to='funny/funnyParagraph/', verbose_name='图片路径')),
                ('pContent', models.TextField(blank=True, max_length=5000, null=True, verbose_name='内容')),
            ],
            options={
                'verbose_name': '搞笑段子',
                'verbose_name_plural': '搞笑段子',
            },
        ),
        migrations.CreateModel(
            name='HumorousJokeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pContent', models.TextField(blank=True, max_length=5000, null=True, verbose_name='内容')),
            ],
            options={
                'verbose_name': '幽默笑话',
                'verbose_name_plural': '幽默笑话',
            },
        ),
    ]