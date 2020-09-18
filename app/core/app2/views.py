from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import ImpresoraDjango

from django.views.generic import ListView, DeleteView, UpdateView, CreateView

# Create your views here.

class IndexView(ListView):
  model =  ImpresoraDjango
  context_object_name = 'impresoraList'
  template_name = 'index.html'

class IndexCreate(CreateView):
  model = ImpresoraDjango
  template_name = 'create.html'
  fields = [
    # 'id',
    'nombre_impresora',
    'modelo',
    'marca',
    'fecha_compra',
    'ultimo_mantenimiento',
    'ubicacion_fisica',
    'nombre_responsable',
    'correo_responsable',
    'ip'
  ]
  success_url = reverse_lazy('impresoras:index')

class IndexDelete(DeleteView):
  model = ImpresoraDjango
  context_object_name = 'impresora'
  template_name = 'delete.html'
  success_url = reverse_lazy('impresoras:index')

class IndexUpdate(UpdateView):
  model =  ImpresoraDjango
  template_name = 'create.html'
  fields = [
    # 'id',
    'nombre_impresora',
    'modelo',
    'marca',
    'fecha_compra',
    'ultimo_mantenimiento',
    'ubicacion_fisica',
    'nombre_responsable',
    'correo_responsable',
    'ip'
  ]
  success_url = reverse_lazy('impresoras:index')

  # def get_context_data(self, **kwargs):
  #       context = super(IndexUpdate, self).get_context_data(**kwargs)
  #       context['update'] = True
  #       return context



# cambio de funciones por vistas 
# def buscar( request  ):
#   return render( request, 'index.html' )

# def resultado( request ):
#   mensaje = 'Busaqueda del input: %r' %request.GET['impresora']
#   # return render( request, 'resultado.html')
#   return HttpResponse(mensaje)