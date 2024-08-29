from django.shortcuts import render
from costumer.models import Costumer
from internet_app.models import Internet
from provider.models import Provider
from django.http.response import JsonResponse
import json

def register_costumer(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        costumer = Costumer.objects.create(name=name, phone=phone)
        costumer.save()
        return JsonResponse({'status': 'success'}, safe=False)
    else:
        return JsonResponse('error', safe=False)
    
def buy_internet(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        costumer = Costumer.objects.get(id=data['costumer_id'])
        internet = Internet.objects.get(id=data['internet_id'])
        if costumer.wallet >= internet.price:
            costumer.wallet -= internet.price
            costumer.bought_internet.add(internet)
            costumer.save()
            return JsonResponse({'status': 'success'}, safe=False)
        else:
            return JsonResponse({'status': 'not enough money'}, safe=False)
    else:
        return JsonResponse('error', safe=False)