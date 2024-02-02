# deep_app의 urls.py
from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('input_image/', views.input_image, name='input_image'),
    path('file_upload/', foodInfoOneAPI_Return_INFO, name='file_upload'),
    path('input_image/result/', views.result, name='result'),
    # 수업 예시
    path('hello/', helloAPI),
    path('res/', RestaurantInfoAPI),
    path('food/', foodInfoAPI),
    path('food/<str:food_name>/', foodInfoOneAPI),
]
