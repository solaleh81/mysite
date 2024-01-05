from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('single/<int:id>', views.blog_single, name='single'),
    path('category/<str:cat_name>', views.blog_category, name='category'),
    path('test', views.test, name='test'),

]
