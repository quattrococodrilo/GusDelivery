# Factory boy
import factory
from factory.django import DjangoModelFactory

# Models 
from postal_codes.models import Estado

# Utils
from random import sample

class EstadoFactory(DjangoModelFactory):
    """ Crea estados ficticios. """

    class Meta:
        model = Estado
        django_get_or_create = ['d_estado', 'c_estado']

    d_estado = factory.Faker('street_name')
    c_estado = lambda: sample(range(10000), 1)
