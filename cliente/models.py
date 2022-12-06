from django.db import models
from home.models import Pessoa

# Create your models here.
class Cliente(Pessoa):
    endereco = models.CharField('Endereço', max_length=100, help_text='Endereço contato')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome', ]

    def __str__(self):
        return super().nome