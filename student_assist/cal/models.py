from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    date = models.DateTimeField()
    due_date = models.DateTimeField()
    duration = models.DurationField()
    elapsed = models.DurationField()
    
