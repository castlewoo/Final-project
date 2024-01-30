# deep_app의 urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('input_image/', views.input_image, name='input_image'),
    path('file_upload/', views.file_upload, name='file_upload'),
    path('input_image/result/', views.result, name='result'),
]
