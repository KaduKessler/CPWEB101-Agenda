from django.urls import path
from .views import AtendimentoView

urlpatterns = [
    path('atendimentos', AtendimentoView.as_view(), name='atendimentos'),
]