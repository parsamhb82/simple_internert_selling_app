from django.contrib.admin import register, ModelAdmin
from provider.models import Provider

@register(Provider)
class ProviderAdmin(ModelAdmin):
    pass

