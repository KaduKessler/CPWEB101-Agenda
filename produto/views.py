from django.core.paginator import Paginator
from django.views.generic import ListView
from produto.models import Produto


# Create your views here.
class ProdutosView(ListView):
    model = Produto
    template_name = 'produtos.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ProdutosView, self).get_queryset(*args, **kwargs)

        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        #return qs
        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem
