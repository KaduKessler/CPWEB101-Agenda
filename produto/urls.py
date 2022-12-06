from django.urls import path
from .views import ProdutosView

urlpatterns = [
    path('produtos', ProdutosView.as_view(), name='produtos'),
]