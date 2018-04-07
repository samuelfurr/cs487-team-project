from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import connection
# Create your views here.

# TODO: Actually integrate the views with HTML pages once the pages
# get more fleshed out.

def feed(request):
    return render(request, 'feed/feed.html')

# Will eventually have to process displaying the feed.  This is going to
# entail the following:

# 1. As usual, check for a proper post request.  Throw an error on
# malformed POST data.

# 2. Pull tasks/breaks that correspond to 3 hours prior/24 hours after
# the current time.  Pull motivational quotes that have not been used
# in at least 3 days.  Update quote usage stats for the quotes.

# 3. Run the scheduling algorithm based on the current schedule to
# schedule any new events (aka events that weren't in the time period
# the last time the page was loaded)

# 4. Build a list of events/breaks/quotes to be returned to the
# renderer.  This can just be a simple list, the renderer can handle
# inserting them in appropriate places, etc.
