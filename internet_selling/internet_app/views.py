from django.shortcuts import render
from internet_app.models import Internet
from django.http.response import JsonResponse, FileResponse
import json
from costumer.models import Costumer
from io import BytesIO

def view_internet(request):
    internets = Internet.objects.all()
    internets_list = []
    for internet in internets:
        internets_list.append({
            'price': internet.price,
            'name': internet.name,
        }
        )
    return JsonResponse(internets_list, safe=False)

def all_bought_internet(request):
    costumers = Costumer.objects.all()
    internet_list = []
    for costumer in costumers:
            internet_list.append({
            'name': costumer.name,
            'bought_internet': list(costumer.bought_internet.all().values())
        }
        )
    json_data = json.dumps(internet_list)  
    buffer = BytesIO()
    buffer.write(json_data.encode('utf-8'))  # Write JSON data to buffer
    buffer.seek(0)

    response = FileResponse(buffer, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="bought_internet.json"'
    return response
    

    
