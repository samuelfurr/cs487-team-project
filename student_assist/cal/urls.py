from django.conf.urls import url
from django.contrib import admin
from cal import views

urlpatterns = [
    # URL patterns correspond to their views in views.py<cal>
    url(r'^$', views.cal, name = 'cal'),
    url(r'^add/$', views.add, name = 'add'),
]
