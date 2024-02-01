# deep_app의 urls.py
from django.urls import path
from . import views
from .views import helloAPI

app_name = 'about'

urlpatterns = [
    path('', views.outline, name='outline'),
    path('hello/', helloAPI)
]
