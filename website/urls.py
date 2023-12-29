from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('http-test', views.http_test, name='http'),
    path('json-test', views.json_test, name='json'),

]