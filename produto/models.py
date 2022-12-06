from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome do produto')
    preco = models.DecimalField('Preço', max_digits=6, decimal_places=2, help_text='Preço do produto')
    fornecedor = models.CharField('Fornecedor', max_length=50, help_text='Nome do fornecedor')
    quantidade = models.DecimalField('Quantidade', max_digits=5, decimal_places=2, help_text='Quantidade em estoque')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome', ]

    def __str__(self):
        return self.nome
