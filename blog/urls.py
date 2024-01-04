from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('single', views.blog_single, name='single'),
    path('test', views.test, name='test'),

]