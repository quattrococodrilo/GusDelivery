# Factory boy
import factory
from factory import SubFactory
from factory.django import DjangoModelFactory

# Models
from postal_codes.models import CodigoPostal

# Factories
from .estados_factory import EstadoFactory
from .municipios_factory import MunicipioFactory
from .asentamientos_factory import AsentamientoFactory

class PostalCodeFactory(DjangoModelFactory):
    """ Crea estados ficticios. """

    class Meta:
        model = CodigoPostal 
        django_get_or_create = [
            'd_codigo',
            'd_estado',
            'd_mnpio',
            'd_asenta',
        ]

    d_codigo = factory.Faker('postcode') 
    d_estado = SubFactory(EstadoFactory) 
    d_mnpio = SubFactory(MunicipioFactory)
    d_asenta = SubFactory(AsentamientoFactory)