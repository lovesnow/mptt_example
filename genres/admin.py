#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Genre
from mptt.admin import MPTTModelAdmin



admin.site.register(Genre, MPTTModelAdmin)



