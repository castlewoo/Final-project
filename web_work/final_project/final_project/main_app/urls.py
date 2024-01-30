# urls.py
# 이 두줄은 외우자
from django.urls import path
from . import views

urlpatterns = [
    # main/
    path('', views.index, name='index'),
    path('login/', views.login, name='login')
]
######