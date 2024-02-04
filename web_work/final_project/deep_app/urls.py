# deep_app의 urls.py
from django.urls import path
from . import views

app_name = 'deep_app'

urlpatterns = [
    path('input_image/', views.input_image, name='input_image'),
    path('file_upload/', views.foodInfoOneAPI_Return_INFO, name='file_upload'),
    path('input_image/result/', views.foodInfoOneAPI_Return_INFO, name='result'),
    
    path('food_map_form/', views.food_map_form, name='food_map_form'),
    path('show_res_map/', views.show_res_map, name='show_res_map'),
]
