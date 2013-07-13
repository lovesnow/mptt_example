#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name="children")
    
    class MPTTMeta:
        order_insertion_by = ['name']
        
    class Meta:    
        verbose_name = "流派"
        verbose_name_plural = "流派"
        
    def __unicode__(self):    
        return self.name
    
