from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from core.forms import PessoaForm
from core.models import Pessoa


# Create your views here.

class Home(ListView):
    template_name = "home.html"
    model = Pessoa
    queryset = Pessoa.objects.all()


class HomeForm(CreateView):
    template_name = "home_form.html"
    model = Pessoa
    form_class = PessoaForm
    context_object_name = 'forms'
    success_url = reverse_lazy('teste')

    def form_invalid(self, form):
        form = super(HomeForm, self).form_invalid(form)
        print(form)
        return form

class HomeUpdateForm(UpdateView):
    template_name = "home_form.html"
    model = Pessoa
    form_class = PessoaForm
    context_object_name = 'forms'
    success_url = reverse_lazy('teste')

    def form_invalid(self, form):
        form = super(HomeForm, self).form_invalid(form)
        print(form)
        return form
