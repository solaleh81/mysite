from django.contrib import admin
from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index_view, name='home'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('newsletter', views.news_letter, name='newsletter'),
    path('test', views.test_view, name='test'),

]