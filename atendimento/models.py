from django.db import models

# Create your models here.
class Atendimento(models.Model):
    SITUACAO_OPCOES = (
        ('A', 'Agendado'),
        ('B', 'Realizado'),
        ('C', 'Cancelado')
    )

    horario = models.DateTimeField('Horário',
                                   help_text='Data e hora atendimento')

    cliente = models.ForeignKey('cliente.Cliente',
                                verbose_name='Cliente',
                                help_text='Nome do cliente',
                                on_delete=models.CASCADE)

    funcionario = models.ForeignKey('funcionario.Funcionario',
                                    verbose_name='Funcionário',
                                    help_text='Nome do funcionário',
                                    on_delete=models.CASCADE)

    situacao = models.CharField('Situação',
                                max_length=15,
                                help_text='Situação do atendimento',
                                choices=SITUACAO_OPCOES,
                                default='A')

    servico = models.ForeignKey('servico.Servico',
                                verbose_name='Serviço',
                                help_text='Nome do serviço',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
        ordering = ['-horario', ]

    def __str__(self):
        return f'Cliente: {self.cliente} - Funcionário: {self.funcionario} - Serviço: {self.servico}'
