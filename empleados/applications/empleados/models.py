from django.db import models

# Create your models here.
#Modelo
from applications.departamentos.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    def __str__(self):
        return str(self.id) + " " + self.habilidad

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'


class Trabajo(models.Model):
    trabajo = models.CharField('Trabajo', max_length=50)

    def __str__(self):
        return str(self.id) + " " + self.trabajo

    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'


class Empleado(models.Model):
    SEXO_CHOICES = (
        ('V', 'Varon'),
        ('M', 'Mujer'),
        ('O', 'Otro'),
    )
    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="empleados", blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)

    def __str__(self):
        return self.nombres + " - " + self.apellidos

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

