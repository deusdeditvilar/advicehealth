from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def Teste(request):
    people = Person.objects.all()
    return render(request,'dashboard.html',{'people':people})