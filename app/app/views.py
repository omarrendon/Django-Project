from django.http import HttpResponse
from django.shortcuts import render

def index( request ):
  return render(request, 'index.html', {
    # context
    'message': 'nuevo mensaje desde la vista',
    'productos': [
      {'title': 'Playera', 'price': 5, "stock": True },
      {'title': 'Camisa', 'price': 3, "stock": True },
      {'title': 'Jeans', 'price': 2, "stock": False },
    ]
  })
