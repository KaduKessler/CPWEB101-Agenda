from django.views.generic import ListView
from .forms import AtendimentoListForm
from .models import Atendimento

class AtendimentoView(ListView):
    model = Atendimento
    template_name = 'atendimentos.html'

    def get_context_data(self, **kwargs):
        context = super(AtendimentoView, self).get_context_data(**kwargs)

        if self.request.GET:
            form = AtendimentoListForm(self.request.GET)
        else:
            form = AtendimentoListForm()

        context['form'] = form

        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(AtendimentoView, self).get_queryset()

        if self.request.GET:
            form = AtendimentoListForm(self.request.GET)
            if form.is_valid():
                cliente = form.cleaned_data.get('cliente')
                funcionario = form.cleaned_data.get('funcionario')
                servico = form.cleaned_data.get('servico')
                situacao = form.cleaned_data.get('situacao')

                if cliente:
                    qs = qs.filter(cliente=cliente)

                if funcionario:
                    qs = qs.filter(funcionario=funcionario)

                if servico:
                    qs = qs.filter(servico=servico)

                if situacao != 'T':
                    qs = qs.filter(situacao__icontains=situacao)

        return qs
