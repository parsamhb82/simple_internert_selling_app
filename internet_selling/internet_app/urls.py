from django.urls import path
from internet_app.views import view_internet, all_bought_internet

urlpatterns = [
    path('view_internet/', view_internet),
    path('all_bought_internet/', all_bought_internet),
]