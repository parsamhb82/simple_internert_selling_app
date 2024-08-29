from django.db import models
from internet_app.models import Internet

class Provider(models.Model):
    name = models.CharField(max_length=255, bqlank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    is_active = models.BooleanField(default=False)
    internet = models.ManyToManyField(Internet, on_delete=models.PROTECT, blank=True)
