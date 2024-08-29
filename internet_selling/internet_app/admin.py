from django.contrib.admin import ModelAdmin, register

from internet_app.models import Internet

@register(Internet)
class InternetAdmin(ModelAdmin):
    pass


