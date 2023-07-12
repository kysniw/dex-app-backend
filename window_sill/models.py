from django.db import models

# Create your models here.

class WindowSill(models.Model):
    sill_name = models.CharField(max_length=255)
