from django.db import models

# Create your models here.

class Lists(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Nombre de la lista')
    is_active = models.BooleanField(default = True, verbose_name = 'Activo')
    
    def __str__(self):
        return f'{self.name}'


class Tasks(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Nombre de tarea')
    start_date = models.DateTimeField(blank = True, null = True, verbose_name = 'Fecha de inicio')
    list = models.ForeignKey(Lists, on_delete = models.CASCADE, verbose_name = 'Lista')
    priority = models.CharField(max_length = 1, choices = (('H','Alta'), ('M', 'Media'), ('L', 'Baja')), verbose_name = 'Prioridad')
    status = models.BooleanField(default = False, verbose_name = 'Estado') #false es pendiente y true completado
    is_active = models.BooleanField(default = True, verbose_name = 'Activo')
    
    def __str__(self):
        return f'{self.name} {self.start_date}'

