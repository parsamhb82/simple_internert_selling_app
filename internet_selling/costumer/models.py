from django.db import models
from internet_app.models import Internet

class Costumer(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    wallet = models.IntegerField(default=100000)
    bought_internet = models.ManyToManyField(Internet, blank=True)