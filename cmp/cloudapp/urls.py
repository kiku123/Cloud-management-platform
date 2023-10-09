from django.contrib import admin
from django.urls import path
from cloudapp import views

admin.site.site_header = "CMP Admin"
admin.site.site_title = "CMP Admin Portal"
admin.site.index_title = "Welcome to Cloud Management Platform"

urlpatterns = [
    path('', views.index, name = 'home'),
    path('resource', views.resource, name = 'resource'),
    path('alert', views.alert, name = 'alert'),
    path('management', views.management, name = 'management'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('logout', views.logout, name = 'logout')
]
