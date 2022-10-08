from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Person(models.Model):
    nome = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nome)

class Car(models.Model):
    COLOR_CHOICES = (
        ('Amarelo','Amarelo'),
        ('Azul','Azul'),
        ('Cinza','Cinza')
    )
    TYPE_CHOICES = (
        ('Hatch','Hatch'),
        ('Sedan','Sedan'),
        ('Conversível','Conversível')
    )
    pessoa = models.ForeignKey(Person,on_delete=models.CASCADE,related_name="person_car")
    cor = models.CharField(max_length=50,choices=COLOR_CHOICES)
    modelo = models.CharField(max_length=50,choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.modelo,self.cor)
    
    def clean(self):
        cor = Car.objects.filter(pessoa_id=self.pessoa_id,cor=self.cor)
        modelo = Car.objects.filter(pessoa_id=self.pessoa_id,modelo=self.modelo)
        if cor or modelo:
            raise ValidationError('{} já tem cor ou modelo desse tipo'.format(self.pessoa))            
        if Car.objects.filter(pessoa_id=self.pessoa_id).count() >= 3:
            raise ValidationError('{} já tem o máximo de carros permitidos'.format(self.pessoa))