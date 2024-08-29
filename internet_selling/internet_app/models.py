from django.db import models

class Internet(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.IntegerField(default=1000)
