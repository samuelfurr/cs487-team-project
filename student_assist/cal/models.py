from django.db import models
from datetime import timedelta

# Create your models here.
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.CharField(max_length=255, default="None")
    due_date = models.DateTimeField()
    duration = models.DurationField()
    all_day = models.NullBooleanField()

    def clean(self):
        if self.all_day and self.duration != timedelta(days=1):
            raise ValidationError("All day events must be 1 day long!")

class Break(models.Model):
   task = models.ForeignKey('Task', on_delete=models.CASCADE, primary_key=True)
   date = models.DateTimeField()
   duration = models.DurationField()

   class Meta:
       unique_together = (('task', 'date'),)
