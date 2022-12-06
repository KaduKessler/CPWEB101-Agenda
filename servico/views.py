from django.views.generic import ListView
from .models import Servico


# Create your views here.
class ServicosView(ListView):
    model = Servico
    template_name = 'servicos.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ServicosView, self).get_queryset(*args, **kwargs)

        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs
