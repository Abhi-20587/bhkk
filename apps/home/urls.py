# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

from .views import Home_g,Add_Student,Delete_Student,EditStudent


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('abhitable', Home_g.as_view(), name='abhitable'),
    path('add-student', Add_Student.as_view(), name='add-student'),
    path('delete-student', Delete_Student.as_view(), name='delete-student'),
    path('edit-student/<int:id>/', EditStudent.as_view(), name='edit-student'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
