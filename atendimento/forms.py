from django import forms

from cliente.models import Cliente
from funcionario.models import Funcionario
from servico.models import Servico

class AtendimentoListForm(forms.Form):
    SITUACAO_OPCOES = (
        ('T', '----------'),
        ('A', 'Agendado'),
        ('R', 'Realizado'),
        ('C', 'Cancelado')
    )

    cliente = forms.ModelChoiceField(label='Cliente: ', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), queryset=Cliente.objects.all(), required=False)

    funcionario = forms.ModelChoiceField(label='Funcionário: ', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), queryset=Funcionario.objects.all(), required=False)

    servico = forms.ModelChoiceField(label='Serviço: ', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), queryset=Servico.objects.all(), required=False)

    situacao = forms.ChoiceField(label='Situação: ', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), choices=SITUACAO_OPCOES, required=False)
