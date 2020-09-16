from django.shortcuts import render
from django.http import HttpResponse

from .models import ImpresoraDjango

from django.views.generic import ListView, DeleteView, UpdateView, DetailView

# Create your views here.

class IndexView(ListView):
  model =  ImpresoraDjango
  context_object_name = 'impresoraList'
  template_name = 'index.html'


# def buscar( request  ):
#   return render( request, 'index.html' )

# def resultado( request ):
#   mensaje = 'Busaqueda del input: %r' %request.GET['impresora']
#   # return render( request, 'resultado.html')
#   return HttpResponse(mensaje)