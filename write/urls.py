from django.urls import path
from . import views

urlpatterns = [
    path('', views.write, name='write'),
    path('balance/', views.balance, name='balance'),
]
