# deep_app의 urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.deep, name='deep')
]
