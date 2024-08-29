from django.urls import path
from provider.views import register_provider, add_internet

urlpatterns = [
    path('register_provider/', register_provider),
    path('add_internet/', add_internet),
]