from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
# Create your views here.

def Dashboard(request):
    people = Person.objects.all()
    return render(request,'dashboard.html',{'people':people})

class PersonCreateView(CreateView):
    model = Person
    template_name = 'add_person.html'
    fields = ['nome']