from django.db import models

# Create your models here.

class Quote(models.Model):
    quote_id = models.AutoField(primary_key=True)
    text = models.TextField(default="")
    author = models.CharField(max_length=255)
    last_used = models.DateTimeField()
