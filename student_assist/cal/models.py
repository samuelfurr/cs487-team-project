from django.db import models
from datetime import timedelta

# Create your models here.

# This task object is for tasks the user has to complete, as well as
# other events like dinner, concerts, etc.
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

# Breaks get sprinkled into longer assignments the users have.
# Many-to-one relationship with a Task.
class Break(models.Model):
   task = models.ForeignKey('Task', on_delete=models.CASCADE, primary_key=True)
   date = models.DateTimeField()
   duration = models.DurationField()

   class Meta:
       unique_together = (('task', 'date'),)

# TODO: Add more models as needed for the calendar
