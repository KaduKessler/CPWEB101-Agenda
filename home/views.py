from django.views.generic import TemplateView
from atendimento.models import Atendimento
from cliente.models import Cliente
from funcionario.models import Funcionario
from produto.models import Produto
from servico.models import Servico


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['qtd_clientes'] = Cliente.objects.count()
        context['qtd_funcionarios'] = Funcionario.objects.count()
        context['qtd_servicos'] = Servico.objects.count()
        context['qtd_produtos'] = Produto.objects.count()
        context['qtd_atendimentos'] = Atendimento.objects.count()
        return context
    