from django.db import models

# Create your models here.
class Convert(models.Model):
    name = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    editFlg = models.BooleanField(default=False)