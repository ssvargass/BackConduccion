# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldoption',
            name='name',
        ),
        migrations.AddField(
            model_name='fieldoption',
            name='key',
            field=models.CharField(default='', max_length=255, verbose_name='Llave'),
        ),
        migrations.AddField(
            model_name='fieldoption',
            name='value',
            field=models.CharField(default='', max_length=255, verbose_name='Valor'),
        ),
    ]
