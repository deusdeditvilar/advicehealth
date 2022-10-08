import django_filters
from django import forms
from .models import Person

class PersonFilter(django_filters.FilterSet):
    nome = django_filters.filterset.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-control form-control-lg border-0 add-todo-input bg-transparent rounded','placeholder':"Pesquisar pessoas"}))

    class Meta:
        model = Person
        fields = ['nome']