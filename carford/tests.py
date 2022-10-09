from django.test import TestCase
from .models import Person, Car
from django.core.exceptions import ValidationError, FieldError

# Create your tests here.
class PersonTestCase(TestCase):
    def testPerson(self):
        for i in range(1001):
            person = Person.objects.create(nome="Teste_{}".format(i))
            self.assertEqual(person.nome, "Teste_{}".format(i))


class CarTestCase(TestCase):

    def testCar(self):
        person = Person.objects.create(nome="João Bobão")
        car = Car.objects.create(cor='Amarelo',modelo='Hatch',pessoa=person)
        self.assertEqual(car.cor,'Amarelo')
        self.assertEqual(car.modelo,'Hatch')
        self.assertEqual(car.pessoa.nome,'João Bobão')
        

        car_second = Car.objects.create(cor='Azul',modelo='Sedan',pessoa=person)
        self.assertIsNot(car_second.cor,'Amarelo')
        self.assertEqual(car_second.modelo,'Sedan')
        self.assertEqual(car_second.pessoa.nome,'João Bobão')
        
        ''' ADICIONANDO CARRO COM COR QUE NÃO EXISTE '''
        try:
            Car.objects.create(cor='Rosa',modelo='Conversível',pessoa=person)
        except ValidationError as e:
            self.assertTrue('cor' in e.message_dict)
        
        ''' TENTANDO ADICIONAR CARRO COM MODELO E COR JÁ ADICIONADOS '''
        try:
            Car.objects.create(cor='Azul',modelo='Hatch',pessoa=person)
        except FieldError as e:
            self.assertAlmostEqual(str(e),'{} já tem cor ou modelo desse tipo'.format(person.nome))
        
        car_third = Car.objects.create(cor='Cinza',modelo='Conversível',pessoa=person)
        self.assertEqual(car_third.cor,'Cinza')
        self.assertEqual(car_third.modelo,'Conversível')
        self.assertEqual(car_third.pessoa.nome,'João Bobão')
        