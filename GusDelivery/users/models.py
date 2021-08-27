from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """ Esta clase se encarga de los usuarios registrados. 
    Permite agregar campos, así como cambiar las estrategias de autenticación """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        },
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username
