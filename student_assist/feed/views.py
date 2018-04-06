from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import connection
# Create your views here.


def feed(request):
    return render(request, 'feed/feed.html')

