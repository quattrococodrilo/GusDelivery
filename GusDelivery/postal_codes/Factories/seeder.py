# Django
from django.db import IntegrityError

# Factories
from .estados_factory import EstadoFactory
from .municipios_factory import MunicipioFactory
from .asentamientos_factory import AsentamientoFactory
from .postalcodes_factory import PostalCodeFactory

class PostalCodeSeeder:
    
    amount = 100

    def __init__(self, amount):
        self.amount = int(amount)
        self.estados()
        self.municipios()
        self.asentamientos()
        self.codigos_postales()

    def generator(self, factory, amount):
        for i in range(int(amount)):
            try:
                factory.create()
            except IntegrityError:
                continue


    def estados(self):
        """ Genera estados ficticios. """
        amount = self.amount
        
        if self.amount > 50:
            amount = self.amount / 2

        self.generator(EstadoFactory, amount)
    
    def municipios(self):
        """ Genera estados ficticios. """
        amount = self.amount * 3

        self.generator(MunicipioFactory, amount)

    def asentamientos(self):
        amount = self.amount * 6

        self.generator(AsentamientoFactory, amount)

    def codigos_postales(self):
        amount = self.amount * 6

        self.generator(PostalCodeFactory, amount)


