from django.shortcuts import render
from costumer.models import Costumer
from internet_app.models import Internet
from provider.models import Provider
from django.http.response import JsonResponse
import json

def register_provider(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        phone = data['phone']
        email = data['email']
        provider = Provider.objects.create(name=name, phone=phone, email = email, is_active=False)
        return JsonResponse({'status': 'success'}, safe=False)
    else:
        return JsonResponse('error', safe=False)
    
def add_internet(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        price = data['price']
        provider = Provider.objects.get(id=data['provider_id'])
        internet = Internet.objects.create(name=name, price=price)
        provider.objects.add(internet)
        provider.save()
        return JsonResponse({'status': 'success'}, safe=False)
    else:
        return JsonResponse('error', safe=False)