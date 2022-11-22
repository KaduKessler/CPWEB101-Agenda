from django.contrib import admin
from django.utils.html import format_html

from .models import Funcionario


# Register your models here.
@admin.register(Funcionario)
class ClienteAdmin(admin.ModelAdmin):
    fields = ('nome', 'funcao', 'data_admissao', 'fone', 'email', 'foto', 'fotografia')
    list_display = ('nome', 'funcao', 'data_admissao')
    readonly_fields = ['fotografia']
    search_fields = ('nome', 'fone')
    list_filter = ('funcao',)

    def fotografia(self, obj):
        if obj.foto:
            return format_html('<img width="150px" src="{}" />', obj.foto.url)
        pass