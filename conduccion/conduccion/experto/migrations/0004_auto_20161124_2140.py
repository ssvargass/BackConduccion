# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experto', '0003_auto_20161124_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field_option',
            field=models.ManyToManyField(related_name='Opciones', to='experto.FieldOption'),
        ),
    ]
