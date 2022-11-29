from django.urls import path
from .views import ClientesView

urlpatterns = [
    path('clientes', ClientesView.as_view(), name='clientes'),
]