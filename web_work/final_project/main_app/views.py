import random
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'main_app/index_food.html')

def input_image(request):
    return render(request, 'main_app/input_image.html')

def result(request):
    return render(request, 'main_app/result.html')
