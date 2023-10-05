from django.contrib import admin
from django.urls import path
from cloudapp import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('resource', views.resource, name = 'resource'),
    path('alert', views.alert, name = 'alert'),
    path('management', views.management, name = 'management'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact')
]
