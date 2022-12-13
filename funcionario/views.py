from django.views.generic import ListView
from funcionario.models import Funcionario
from home.utils import HtmlToPdf

# Create your views here.
class FuncionariosView(ListView):
    model = Funcionario
    template_name = 'funcionarios.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(FuncionariosView, self).get_queryset(*args, **kwargs)

        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='funcionarios_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(FuncionariosView, self).get(*args, **kwargs)
