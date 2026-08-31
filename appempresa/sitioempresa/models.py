from django.db import models

# Create your models here.
class Servicio():
    def __init__(self, id, nombre, descripcion_corta, descripcion_larga, precio, icon, tiempo, item_Uno, item_Due, item_Tre, item_Quattro):
        self.id = id
        self.nombre = nombre
        self.descripcion_corta = descripcion_corta
        self.descripcion_larga = descripcion_larga
        self.precio = precio
        self.icon = icon
        self.tiempo = tiempo
        self.item_Uno = item_Uno
        self.item_Due = item_Due
        self.item_Tre = item_Tre
        self.item_Quattro = item_Quattro
def servicios():
    lista_servicios = [
        Servicio(1, "Desarrollo de sitios web", "Sitios y aplicaciones web a medida, rápidos y responsivos para tu negocio.", "Diseñamos y desarrollamos sitios web y aplicaciones a medida para empresas que necesitan presencia digital profesional. Trabajamos con tecnologías modernas del lado del servidor para que tu sitio sea rápido, seguro y fácil de mantener.", 450000,  "WEB", "3 a 6", "Diseño responsivo para escritorio, tablet y móvil", "Panel de administración de contenidos", "Optimización de velocidad de carga", "Integración con redes sociales y formularios de contacto"),
        Servicio(2, "Aplicaciones Móviles","Apps nativas e híbridas para Android e iOS, conectadas a tus sistemas.","Desarrollamos aplicaciones móviles para Android e iOS conectadas a tus sistemas de backend existentes, pensadas para acompañar a tus clientes desde el celular con la misma calidad que tu plataforma web",890000,"APP", "6 a 10", "Apps nativas e híbridas (Android / iOS)", "Notificaciones push y geolocalización", "Conexión a API REST propia o de terceros", "Publicación en Google Play y App Store"),
        Servicio(3, "Consultoría en la Nube", "Migración y optimización de infraestructura en la nube para tu empresa.", "Ayudamos a tu empresa a migrar y optimizar su infraestructura en servicios en la nube, reduciendo costos operativos y mejorando la disponibilidad de tus sistemas críticos.", 600000,"CLOUD", "2 a 4", "Diagnóstico de infraestructura actual", "Migración de servidores y bases de datos", "Configuración de respaldos automáticos", "Monitoreo y alertas 24/7"),
        Servicio(4, "Ciberseguridad para Pymes", "Protege los datos de tu empresa y de tus clientes con buenas prácticas reales.","Evaluamos la seguridad de tus sistemas y aplicamos buenas prácticas de protección de datos, control de accesos y respuesta ante incidentes, adaptadas a la realidad de una pyme.",350000,"SEC", "2 a 3", "Auditoría básica de vulnerabilidades", "Políticas de contraseñas y control de accesos", "Respaldo y recuperación ante incidentes", "Capacitación al equipo interno"),

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