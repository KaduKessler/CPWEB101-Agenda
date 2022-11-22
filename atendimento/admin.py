from django.contrib import admin
from .models import Atendimento

# Register your models here.
@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ['horario', 'cliente', 'funcionario', 'servico', 'situacao']