app_name = 'carford'

from django.urls import path
from .views import *

urlpatterns = [
    path('', Dashboard),
    path('add/', PersonCreateView.as_view()),
]