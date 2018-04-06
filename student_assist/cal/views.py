from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import connection
# Create your views here.


def cal(request):
    return render(request, 'cal/cal.html')

def add(request):
    return render(request, 'cal/add.html')
