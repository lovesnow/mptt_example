#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
import views 

urlpatterns = patterns(
    "",
    url(r'^$', views.show_genres, name="show_genres"),
)
