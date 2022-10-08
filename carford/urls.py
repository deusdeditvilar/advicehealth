app_name = 'carford'

from django.urls import path
from .views import *

urlpatterns = [
    path('', Dashboard,name='dashboard'),
    path('person/add/', PersonCreateView.as_view(),name='add_pessoa'),
    path('car/add/', CarCreateView.as_view(),name='add_carro'),
]