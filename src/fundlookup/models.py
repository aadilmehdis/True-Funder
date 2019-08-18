from django.db import models

# Create your models here.
class Party(models.Model):
    name    = models.CharField("Name", max_length=120)
    address = models.CharField("Address", max_length=500)
    symbol  = models.CharField("Symbol", max_length=500,null=True)