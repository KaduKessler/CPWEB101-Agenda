from django.views.generic import ListView

from home.utils import HtmlToPdf
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

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='servicos_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ServicosView, self).get(*args, **kwargs)
