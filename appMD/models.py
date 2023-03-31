from django.db import models
from django.utils.html import format_html
from .choices import sexos, opciones
from django.utils import timezone
import datetime
# from Google import Create_Service, convert_to_RFC_datetime




# Create your models here.

paciente_sexo=[
    ("M", 'Masculino'),
    ("F", 'Femenino')
]

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    cedula = models.CharField(max_length=11, verbose_name="Cédula")
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=11, null=False, blank=False, choices= paciente_sexo, verbose_name="Sexo")
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    celular = models.CharField(max_length=10, verbose_name="Celular")
    correo = models.EmailField(max_length=254, null= True, verbose_name="Correo Electrónico")

    def __str__(self):
        fila= "Nombres: " + self.nombres + "  " + self.apellidos + " - " + "Cédula: " + self.cedula
        return fila

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    cedula = models.CharField(max_length=11, verbose_name="Cédula")
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=1, verbose_name="Sexo")
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    celular = models.CharField(max_length=10, verbose_name="Celular")
    correo = models.EmailField(max_length=254, null= True, verbose_name="Correo Electrónico")
    nUsuario = models.CharField(max_length=50, verbose_name="Nombre de Usuario",null= True)
    contrasenia = models.CharField(max_length=100, verbose_name="Contraseña",null= True)
    rol = models.CharField(max_length=50, verbose_name="Sexo",null= False, blank=False)

class Enfermedad(models.Model):
    id = models.AutoField(primary_key=True)
    antibioticosAlergia= models.CharField(max_length=1, choices=opciones, default='N')
    anestesiaAlergia= models.CharField(max_length=1, choices=opciones, default='N')
    hemorragias= models.CharField(max_length=1, choices=opciones, default='N')
    sida= models.CharField(max_length=1, choices=opciones, default='N')
    tuberculosis= models.CharField(max_length=1, choices=opciones, default='N')
    asma= models.CharField(max_length=1, choices=opciones, default='N')
    diabetes= models.CharField(max_length=1, choices=opciones, default='N')
    cardiacas= models.CharField(max_length=1, choices=opciones, default='N')
    otros = models.TextField(max_length=200, verbose_name="Otros", blank=False)
    def __str__(self):
        fila= "enfermedad: " + self.asma + " - " + "otra: " + self.otros
        return fila 

class Historia(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete= models.CASCADE,verbose_name="Codigo del paciente")
    motivoConsulta = models.TextField(max_length=200, verbose_name="Motivo Consulta", blank=False)
    # enfermedad = models.ForeignKey(Enfermedad, null=True, blank=True, on_delete= models.CASCADE, verbose_name="Enfermedad")
    def __str__(self):
        fila= "paciente: " + self.paciente.nombres + " - " + "motivo: " + self.motivoConsulta
        return fila 

class Cita(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    patient = models.ForeignKey(Paciente,on_delete=models.CASCADE)
    objet = models.CharField(max_length=255, blank=True)
    class Meta:
        ordering = ["-date","heure"]
    def ultimasCitas(self):
        return self.date>=timezone.now() - datetime.timedelta(days=1)