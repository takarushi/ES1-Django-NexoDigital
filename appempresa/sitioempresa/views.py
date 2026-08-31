from django.shortcuts import render

# Create your views here.
def sitioempresa_index(request):
 return render(request, "index.html")

def sitioempresa_servicios(request):
 return render(request, "servicios.html")

def sitioempresa_nosotros(request):
 return render(request, "nosotros.html")
def sitioempresa_contacto(request):
 return render(request, "contacto.html")