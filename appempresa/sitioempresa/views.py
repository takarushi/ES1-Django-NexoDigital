from django.shortcuts import render, get_object_or_404 # Aportado por Claude
from sitioempresa.models import  servicios, get_servicio
from django.http import Http404 # Aportado por Claude
from django.views import View

# Create your views here.
def sitioempresa_index(request):
    context = {
        'servicios': servicios()
    }
    return render(request, "index.html", context)

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
    def get(self, request, id):
        servicio = get_servicio(id) #Aportado por Claude empieza aquí
        if servicio is None:
            raise Http404('Servicio no encontrado') #Aportado por Claude termina aqui
        context = {
            'servicio': servicio # Corregido por Claude
        }
        return render(request, "detalle_Servicio.html", context)