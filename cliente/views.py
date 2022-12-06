from django.core.paginator import Paginator
from django.views.generic import ListView
from cliente.models import Cliente


# Create your views here.
class ClientesView(ListView):
    model = Cliente
    template_name = 'clientes.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ClientesView, self).get_queryset(*args, **kwargs)

        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        
        #return qs
        paginator = Paginator(qs, 5)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem