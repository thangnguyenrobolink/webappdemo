from django.db import models

# Create your models here.
class Device(models.Model):
  info = models.CharField(max_length=255)
