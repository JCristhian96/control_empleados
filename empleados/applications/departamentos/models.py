from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(
        'Nombre Departamento',
        max_length=50
        )
    nombre_corto = models.CharField(
        'Nombre Corto Departamento',
        max_length=50
        )
    anulado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre + " " +self.nombre_corto

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'