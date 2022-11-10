from django.db import models

# Create your models here.
# model for storing the results of the task
class Result(models.Model):
    task_id = models.CharField(max_length=255)
    result = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    date_start = models.DateTimeField(null=True)
    date_done = models.DateTimeField(null=True)
