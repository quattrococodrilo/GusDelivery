# Factory boy
import factory
from factory.django import DjangoModelFactory

# Models
from postal_codes.models import Asentamiento

# Utils
from random import sample, randrange

# Faker
from faker import Factory

faker = Factory.create()

class AsentamientoFactory(DjangoModelFactory):
    """ Crea estados ficticios. """

    class Meta:
        model = Asentamiento
        django_get_or_create = [
            'd_asenta',
            'id_asenta_cpcons'
        ]

    d_asenta = factory.Faker('street_name')
    id_asenta_cpcons = factory.Faker('building_number')
    d_tipo_asenta = factory.Faker('word')
    c_tipo_asenta = factory.Faker('building_number')
    d_cp = factory.Faker('postcode')
    d_oficina = factory.Faker('postcode')
    d_zona = lambda: sample(['Urbano', 'Rural'], 1)