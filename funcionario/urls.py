from django.urls import path
from .views import FuncionariosView, FuncionarioAddView

urlpatterns = [
    path('funcionarios', FuncionariosView.as_view(), name='funcionarios'),
    path('funcionario/adicionar', FuncionarioAddView.as_view(), name='funcionario_adicionar')
]