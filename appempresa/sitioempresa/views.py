from django.shortcuts import render
from sitioempresa.models import  servicios
from django.views import View

# Create your views here.
def sitioempresa_index(request):
    context = {
        'servicios': servicios()
    }
    return render(request, "index.html", context)

def sitioempresa_servicios(request):
 return render(request, "servicios.html")

def sitioempresa_nosotros(request):
 return render(request, "nosotros.html")
def sitioempresa_contacto(request):
 return render(request, "contacto.html")

def sitioempresa_servicios(request):
    context = {
        'servicios': servicios()
    }
    return render(request, "servicios.html", context)
class sitioempresa_ViewService(View):
    def get(self, request):
        context = {
            'servicios': servicios()
        }
        return render(request, "servicios.html", context)