from django.contrib import admin
from .models import Evento
#from .models import Usuario

'''
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','email','fecha_creacion','fecha_actualizacion')
    search_fields = ['nombre','apellido','email']
admin.site.register(Usuario, UsuarioAdmin)
'''

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre','usuario','categoria','modo','fecha_inicio','fecha_fin')
    list_filter = ['fecha_inicio','usuario']
    search_fields = ['nombre']
admin.site.register(Evento, EventoAdmin)
