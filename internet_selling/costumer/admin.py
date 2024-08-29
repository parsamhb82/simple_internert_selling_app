from django.contrib.admin import register, ModelAdmin

from costumer.models import Costumer

@register(Costumer)
class CostumerAdmin(ModelAdmin):
    pass
