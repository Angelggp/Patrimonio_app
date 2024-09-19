from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    ADMIN = 'admin'
    GESTOR = 'gestor'
    USUARIO = 'usuario'

    ROLE_CHOICES = [
        (ADMIN, 'Administrador'),
        (GESTOR, 'Gestor'),
        (USUARIO, 'Usuario'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ADMIN)

    def __str__(self):
        return self.username