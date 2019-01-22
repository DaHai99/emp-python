"""
Author: lenovo
Date:   2018/7/15
"""
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path('adddb/', views.adddb),
    path('home/', views.home),
    re_path('^add-(?P<nid>\d+)/', views.add),
    re_path('^edit-(?P<nid>\d+)/', views.edit),
    re_path('^dele-(?P<nid>\d+)/', views.dele),
    path('emp_ajax/', views.emp_ajax),
    path('login/', views.login),
]
