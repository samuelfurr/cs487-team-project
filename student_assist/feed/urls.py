from django.conf.urls import url
from django.contrib import admin
from feed import views

urlpatterns = [
    # URL patterns correspond to their views in views.py<feed>
    url(r'^$', views.feed, name = 'feed'),
]
