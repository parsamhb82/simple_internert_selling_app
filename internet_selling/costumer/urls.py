from django.urls import path
from costumer.views import register_costumer, buy_internet

urlpatterns = [
    path('register_costumer/', register_costumer,),
    path('buy_internet/', buy_internet),
]