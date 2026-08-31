from django.db import models

# Create your models here.
class Servicio():
    def __init__(self, id, nombre, descripcion_corta, descripcion_larga, precio, que_incluye, icon):
        self.id = id
        self.nombre = nombre
        self.descripcion_corta = descripcion_corta
        self.descripcion_larga = descripcion_larga
        self.precio = precio
        self.que_incluye = que_incluye
        self.icon = icon
def servicios():
    lista_servicios = [
        Servicio(1, "Desarrollo de sitios web", "Sitios y aplicaciones web a medida, rápidos y responsivos para tu negocio.", "Diseñamos y desarrollamos sitios web y aplicaciones a medida para empresas que necesitan presencia digital profesional. Trabajamos con tecnologías modernas del lado del servidor para que tu sitio sea rápido, seguro y fácil de mantener.", 450000, "", "WEB"),
        Servicio(2, "Aplicaciones Móviles","Apps nativas e híbridas para Android e iOS, conectadas a tus sistemas.","Desarrollamos aplicaciones móviles para Android e iOS conectadas a tus sistemas de backend existentes, pensadas para acompañar a tus clientes desde el celular con la misma calidad que tu plataforma web",890000,"","APP"),
        Servicio(3, "Consultoría en la Nube", "Migración y optimización de infraestructura en la nube para tu empresa.", "Ayudamos a tu empresa a migrar y optimizar su infraestructura en servicios en la nube, reduciendo costos operativos y mejorando la disponibilidad de tus sistemas críticos.", 600000, "","CLOUD"),
        Servicio(4, "Ciberseguridad para Pymes", "Protege los datos de tu empresa y de tus clientes con buenas prácticas reales.","Evaluamos la seguridad de tus sistemas y aplicamos buenas prácticas de protección de datos, control de accesos y respuesta ante incidentes, adaptadas a la realidad de una pyme.",350000,"","SEC"),

        ]
    return lista_servicios

# Colaborado por Claude Code
# Prompt: "I need help showing some services stored inside models.py and have urls.py
# generate a url for each service inside the directory
#Código generado por Claude empieza aquí:
def get_servicio(id):
    for servicio in servicios():
        if servicio.id == id:
            return servicio
    return None
# Aquí termina código generado por Claude