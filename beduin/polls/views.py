from django.shortcuts import render
from .models import Delivery

def index(request):
    projects = Delivery.objects.all()
    return render(request, 'polls/index.html', {"projects":projects})

def about(request):
    return render(request, 'polls/about.html')

