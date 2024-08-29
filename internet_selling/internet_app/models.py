from django.db import models
from provider.models import Provider
class Internet(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.IntegerField(default=1000)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)
