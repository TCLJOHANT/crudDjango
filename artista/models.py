from django.db import models
from datetime import datetime
# Create your models here.

class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        fila = " id:"+self.id+" nombre: "+ self.nombre+ " genero: "+ self.genero+" Descripcion: "+self.descripcion +"creado:"+self.created_at
        return fila

    class Meta: 
         db_table = 'artista' # cambiará el nombre de la tabla en la base de datos a "artista"
