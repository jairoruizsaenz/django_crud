from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

'''
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    fecha_actualizacion = models.DateTimeField('última actualización', auto_now=True)
    fecha_creacion = models.DateTimeField('fecha creacion', auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)
'''

class Evento(models.Model):
    #{{user.username}}
    #usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    CONFERENCIA = 'CF'
    SEMINARIO = 'SM'
    CONGRESO = 'CG'
    CURSO = 'CS'
    CATEGORIA_OPCIONES = (
        (CONFERENCIA, 'Conferencia'),
        (SEMINARIO, 'Seminario'),
        (CONGRESO, 'Congreso'),
        (CURSO, 'Curso'),
    )
    categoria = models.CharField(max_length=2,choices=CATEGORIA_OPCIONES,default=CONFERENCIA,)

    lugar = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fecha_inicio = models.DateField('fecha inicio',default=datetime.now)
    fecha_fin = models.DateField('fecha fin',default=datetime.now)
    fecha_actualizacion = models.DateTimeField('última actualización', auto_now=True)
    fecha_creacion = models.DateTimeField('fecha creacion',auto_now_add=True)

    PRESENCIAL = 'PR'
    VIRTUAL = 'VR'
    MODO_OPCIONES = (
        (PRESENCIAL, 'Presencial'),
        (VIRTUAL, 'Virtual'),
    )
    modo = models.CharField(max_length=2, choices=MODO_OPCIONES, default=PRESENCIAL, )

    def __str__(self):
        return "%s" % (self.nombre)
'''
    def publish(self):
        self.published_date = timezone.now()
        self.save()
'''