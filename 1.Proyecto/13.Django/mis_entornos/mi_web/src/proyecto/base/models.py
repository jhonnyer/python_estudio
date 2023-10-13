from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    usuario= models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True) #Llave externa
    titulo= models.CharField(max_length=200) #Campo de caracteres
    descripcion=models.TextField(null=True,
                                 blank=True) #Campo de texto
    completo= models.BooleanField(default=False)
    creado=models.DateTimeField(auto_now_add=True) #Se genere automaticamente cuando se crea

    def __str__(self):
        return self.titulo

    #Cuando se pidan las tareas se ordene por medio del campo completo
    class Meta:
        ordering=['completo']