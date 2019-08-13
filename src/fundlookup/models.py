from django.db import models

# Create your models here.
class Party(models.Model):
    name    = models.CharField("Name", max_length=60)
    address = models.CharField("Address", max_length=500)