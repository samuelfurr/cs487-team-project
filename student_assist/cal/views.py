from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import connection
# Create your views here.

# TODO: Actually integrate the views with HTML pages once the pages
# get more fleshed out.

def cal(request):
    return render(request, 'cal/cal.html')
# Will eventually have to process the calendar page.  This is going to
# entail the following:

# 1. As usual, check for a proper post request.  Throw an error on
# malformed POST data.

# 2. Pull the events from the database that are in the current month.
# Easy to do, antyhing matching the month in the date gets pulled.

# 3. Build the dictionary that gets returned to the renderer so that
# the objects can be inserted into the HTML page.  Format will likely
# be something like:
# {'week1': [[task1, break1, task3], [task1, task2, break1], ...], 'week2':...}
# This means we need to split up tasks based on when breaks are in code here.

def add(request):
    return render(request, 'cal/add.html')

# Will have to eventually process adding an event to the calendar
# page.  We can use AJAX for the actual adding so we don't need a
# seperate page for it:

# 1. As usual, check for a proper post request.  Throw an error on
# malformed POST data.

# 2. Duplicate events ARE allowed, so there isn't that much to check
# here.  Basically try to add the event, if the database throws an
# error it means that something was bad with the date/time/etc.

# 3. IF the event was added correctly, add an appropriate number of
# break objects.

# 4. Return the event as added to the DATABASE to the user (and
# breaks), or return an error if adding went wrong.
