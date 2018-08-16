from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Evento

class EventoList(LoginRequiredMixin,ListView):
    model = Evento

    def get_queryset(self):
        return Evento.objects.filter(usuario=self.request.user).order_by('-fecha_creacion')

class EventoDetail(DetailView):
    model = Evento

class EventoCreation(LoginRequiredMixin,CreateView):
    model = Evento
    success_url = reverse_lazy('eventos:list')
    fields = ['nombre', 'categoria', 'lugar', 'direccion', 'fecha_inicio', 'fecha_fin', 'modo']

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class EventoUpdate(LoginRequiredMixin,UpdateView):
    model = Evento
    success_url = reverse_lazy('eventos:list')
    fields = ['nombre', 'categoria', 'lugar', 'direccion', 'fecha_inicio', 'fecha_fin', 'modo']

class EventoDelete(LoginRequiredMixin,DeleteView):
    model = Evento
    success_url = reverse_lazy('eventos:list')
