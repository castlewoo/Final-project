# urls.py
# 이 두줄은 외우자
from django.urls import path
from . import views

urlpatterns = [
    # main/
    path('', views.index, name='index'),
    path('input_image/', views.input_image, name='input_image'),
    path('input_image/result', views.result, name='result'),
]
######