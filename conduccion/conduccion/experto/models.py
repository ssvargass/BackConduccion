# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from imp import reload
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# Create your models here.

class FieldType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Tipo de campo')

    def __str__(self):
        return self.name

class FieldOption(models.Model):
    key = models.CharField(max_length=255, verbose_name='Llave', default="")
    value = models.CharField(max_length=255, verbose_name='Valor', default="")
    def __str__(self):
        return self.key

class Field(models.Model):
    label = models.CharField(max_length=255, verbose_name='Label')
    field_type = models.ForeignKey(FieldType, default=0, related_name="tipo_campo", verbose_name="Tipo de campo")
    field_option = models.ManyToManyField(FieldOption, related_name="Opciones",  blank=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('my_order',)

    def __str__(self):
        return self.label

class FieldCondition(models.Model):
    name = models.CharField(max_length=255, verbose_name='Condicion')
    field = models.ForeignKey(Field, verbose_name='Campo')

    def __str__(self):
        return self.field.label + self.name

class Result(models.Model):
    name = models.CharField(max_length=255, verbose_name='Resultado')
    razon = models.CharField(max_length=255, verbose_name='Razón', blank=True)
    conditions = models.ManyToManyField(FieldCondition, verbose_name="Condiciones")
    def __str__(self):
        return self.name
