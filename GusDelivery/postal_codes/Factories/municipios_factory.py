# Factory boy
import factory
from factory.django import DjangoModelFactory

# Models
from postal_codes.models import Municipio

# Faker
from faker import Factory

faker = Factory.create()

class MunicipioFactory(DjangoModelFactory):
    """ Crea estados ficticios. """

    class Meta:
        model = Municipio
        django_get_or_create = [
            'd_mnpio',
            'c_mnpio',
        ]

    d_mnpio = factory.Faker('street_name') 
    c_mnpio = factory.Faker('building_number')
    d_ciudad = factory.Faker('street_name')
    c_cve_ciudad = factory.Faker('building_number')