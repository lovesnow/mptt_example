#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from mptt.models import TreeForeignKey
from genres.models import Genre

class Product(models.Model):
    name = models.CharField("名称", max_length=50)
    region = TreeForeignKey(Genre, verbose_name="地区")

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品"
        
    def __unicode__(self):    
        return self.name
