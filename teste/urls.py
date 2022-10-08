app_name = 'teste'

from django.urls import path
from .views import *

urlpatterns = [
    path('', Teste),
]