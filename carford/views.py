from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import *
from .filters import *

def Dashboard(request):
    if request.GET:
        filters = request.GET.copy()
        queryset = Person.objects.all().order_by('nome')
        filtro = PersonFilter(filters, queryset=queryset)
    else:
        filtro = PersonFilter(request.GET, queryset=Person.objects.all())
    return render(request,'dashboard.html',{'people':filtro})

class PersonCreateView(CreateView):
    model = Person
    template_name = 'add.html'
    fields = ['nome']
    success_url= reverse_lazy('carford:dashboard')

class CarCreateView(CreateView):
    model = Car
    template_name = 'add.html'
    fields = ['pessoa','modelo','cor']
    success_url= reverse_lazy('carford:dashboard')