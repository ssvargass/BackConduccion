# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experto', '0005_auto_20161124_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field_option',
            field=models.ManyToManyField(blank=True, related_name='Opciones', to='experto.FieldOption'),
        ),
    ]
