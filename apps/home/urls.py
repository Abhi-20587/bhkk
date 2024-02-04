# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

from .views import Home_g


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('abhitable', Home_g.as_view(), name='abhitable'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
