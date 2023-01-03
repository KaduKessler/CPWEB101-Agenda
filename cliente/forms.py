from django import forms
from .models import Cliente

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'fone', 'email', 'foto']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do cliente'}),
            'endereco': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o endereço do cliente'}),
            'fone': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o número do telefone'}),
            'email': forms.EmailInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o e-mail do cliente'}),
            'foto': forms.FileInput(
                attrs={'class': 'input', 'type': 'file'}
            ),
        }