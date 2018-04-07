from django.db import models

# Create your models here.

# This object stores the inspirational/funny quotes that get sprinkled
# throughout the user's feed
class Quote(models.Model):
    quote_id = models.AutoField(primary_key=True)
    text = models.TextField(default="")
    author = models.CharField(max_length=255)
    last_used = models.DateTimeField()

# TODO:  Add more models as needed for the feed
# Particuarly, add schedule model to track current feed schedule
