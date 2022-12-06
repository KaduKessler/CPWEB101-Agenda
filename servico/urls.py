from django.urls import path
from .views import ServicosView

urlpatterns = [
    path('servicos', ServicosView.as_view(), name='servicos'),
]