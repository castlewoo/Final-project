# deep_app의 urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.deep, name='deep'),
    path('input_image/', views.input_image, name='input_image'),
    path('input_image/result', views.result, name='result'),
]
