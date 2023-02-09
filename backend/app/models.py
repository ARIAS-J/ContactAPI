from django.db import models

# Create your models here.

class Contacts(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=60, null=False, blank=False)
    email= models.EmailField(unique=True, null=True, blank=True)
    phone= models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return f"Nombre: {self.nombre} Numero de telefono: {self.phone}"