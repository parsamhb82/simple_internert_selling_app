from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    is_active = models.BooleanField(default=False)
