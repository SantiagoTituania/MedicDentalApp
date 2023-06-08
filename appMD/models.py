import datetime

from django.db import models
from django.utils import timezone
from django.utils.html import format_html

from .choices import opciones, sexos

# from Google import Create_Service, convert_to_RFC_datetime


# Create your models here.

paciente_sexo = [("M", "Masculino"), ("F", "Femenino")]
paciente_enfermedad = [("S", "Si"), ("N", "No")]
paciente_examen_estomatognatico = [("B", "Bueno"), ("M", "Malo")]


class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    cedula = models.CharField(max_length=11, verbose_name="Cédula")
    fechaNacimiento = models.DateField()
    sexo = models.CharField(
        max_length=11,
        null=False,
        blank=False,
        choices=paciente_sexo,
        verbose_name="Sexo",
    )
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    celular = models.CharField(max_length=10, verbose_name="Celular")
    correo = models.EmailField(
        max_length=254, null=True, verbose_name="Correo Electrónico"
    )

    def __str__(self):
        return self.nombres + " " + self.apellidos

    # def __str__(self):
    #     fila = (
    #         "Nombres: "
    #         + self.nombres
    #         + "  "
    #         + self.apellidos
    #         + " - "
    #         + "Cédula: "
    #         + self.cedula
    #     )
    #     return fila


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    cedula = models.CharField(max_length=11, verbose_name="Cédula")
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=1, verbose_name="Sexo")
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    celular = models.CharField(max_length=10, verbose_name="Celular")
    correo = models.EmailField(
        max_length=254, null=True, verbose_name="Correo Electrónico"
    )
    nUsuario = models.CharField(
        max_length=50, verbose_name="Nombre de Usuario", null=True
    )
    contrasenia = models.CharField(max_length=100, verbose_name="Contraseña", null=True)
    rol = models.CharField(max_length=50, verbose_name="Sexo", null=False, blank=False)


class Enfermedad(models.Model):
    id = models.AutoField(primary_key=True)
    antibioticosAlergia = models.CharField(max_length=1, choices=opciones, default="N")
    anestesiaAlergia = models.CharField(max_length=1, choices=opciones, default="N")
    hemorragias = models.CharField(max_length=1, choices=opciones, default="N")
    sida = models.CharField(max_length=1, choices=opciones, default="N")
    tuberculosis = models.CharField(max_length=1, choices=opciones, default="N")
    asma = models.CharField(max_length=1, choices=opciones, default="N")
    diabetes = models.CharField(max_length=1, choices=opciones, default="N")
    cardiacas = models.CharField(max_length=1, choices=opciones, default="N")
    otros = models.TextField(max_length=200, verbose_name="Otros", blank=False)

    def __str__(self):
        fila = "enfermedad: " + self.asma + " - " + "otra: " + self.otros
        return fila


class Historia(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
    )
    motivoConsulta = models.CharField(
        max_length=200, verbose_name="Motivo Consulta", blank=True
    )
    antibioticosAlergia = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=paciente_enfermedad,
        verbose_name="Alergia antibióticos",
    )
    anestesiaAlergia = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_enfermedad,
        verbose_name="Alergia anestesia",
    )
    hemorragias = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_enfermedad,
        verbose_name="Hemorrágias",
    )
    sida = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_enfermedad,
        verbose_name="VIH/SIDA",
    )
    tuberculosis = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_enfermedad,
        verbose_name="Tuberculosis",
    )
    asma = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_enfermedad,
        verbose_name="Asma",
    )
    diabetes = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_enfermedad,
        verbose_name="Diabetes",
    )
    hipertension = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_enfermedad,
        verbose_name="Hipertensión",
    )
    cardiacas = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_enfermedad,
        verbose_name="Enfermedad cardiacas",
    )
    otros = models.TextField(max_length=200, verbose_name="Otros", blank=True)
    fechaTratamiento1 = models.DateField(
        null=True,
    )
    desTratamiento1 = models.CharField(
        max_length=200, verbose_name="Descripcion tratamient 1", blank=True
    )
    fechaTratamiento2 = models.DateField(
        null=True,
    )
    desTratamiento2 = models.CharField(
        max_length=200, verbose_name="Descripcion tratamient 2", blank=True
    )
    fechaTratamiento3 = models.DateField(
        null=True,
    )
    desTratamiento3 = models.CharField(
        max_length=200, verbose_name="Descripcion tratamient 3", blank=True
    )
    fechaTratamiento4 = models.DateField(
        null=True,
    )
    desTratamiento4 = models.CharField(
        max_length=200, verbose_name="Descripcion tratamient 4", blank=True
    )
    # fechaTratamiento5 = models.DateField(
    #     null=True,
    # )
    # desTratamiento5 = models.CharField(
    #     max_length=200, verbose_name="Descripcion tratamient 5", blank=True
    # )
    # fechaTratamiento6 = models.DateField(
    #     null=True,
    # )
    # desTratamiento6 = models.CharField(
    #     max_length=200, verbose_name="Descripcion tratamient 6", blank=True
    # )
    # fechaTratamiento7 = models.DateField(
    #     null=True,
    # )
    # desTratamiento7 = models.CharField(
    #     max_length=200, verbose_name="Descripcion tratamient 7", blank=True
    # )
    # fechaTratamiento8 = models.DateField(
    #     null=True,
    # )
    # desTratamiento8 = models.CharField(
    #     max_length=200, verbose_name="Descripcion tratamient 8", blank=True
    # )
    # fechaTratamiento9 = models.DateField(
    #     null=True,
    # )
    # desTratamiento9 = models.CharField(
    #     max_length=200, verbose_name="Descripcion tratamient 9", blank=True
    # )
    # fechaTratamiento10 = models.DateField(
    #     null=True,
    # )
    # desTratamiento10 = models.CharField(
    #     max_length=200, verbose_name="Descripcion tratamient 10", blank=True
    # )
    # fechaTratamiento11 = models.DateField(
    #     null=True,
    # )
    # desTratamiento11 = models.CharField(
    #     max_length=200, verbose_name="Descripcion tratamient 11", blank=True
    # )
    # fechaTratamiento12 = models.DateField(
    #     null=True,
    # )
    # desTratamiento12 = models.CharField(
    #     max_length=200, verbose_name="Descripcion tratamient 12", blank=True
    # )
    presionArterial = models.CharField(
        max_length=10,
        verbose_name="Presión Arterial",
        null=True,
    )
    frecuenciaCardiaca = models.CharField(
        max_length=10,
        verbose_name="Frecuencia Cardiaca",
        null=True,
    )
    temperatura = models.CharField(
        max_length=10,
        verbose_name="Temperatura",
        null=True,
    )
    frecuenciaRespiratoria = models.CharField(
        max_length=10,
        verbose_name="Frecuencia respiratoria",
        null=True,
    )
    labios = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_examen_estomatognatico,
        verbose_name="Labios",
    )
    mejillas = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_examen_estomatognatico,
        verbose_name="Mejillas",
    )
    maxilarSuperior = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_examen_estomatognatico,
        verbose_name="Maxilar superior",
    )
    maxilarInferior = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_examen_estomatognatico,
        verbose_name="Maxilar Inferior",
    )
    lengua = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_examen_estomatognatico,
        verbose_name="Lengua",
    )
    paladar = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_examen_estomatognatico,
        verbose_name="Paladar",
    )
    piso = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_examen_estomatognatico,
        verbose_name="Piso",
    )
    carrillo = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_examen_estomatognatico,
        verbose_name="Carrillo",
    )
    glandulasSalivales = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_examen_estomatognatico,
        verbose_name="Glándulas salivales",
    )
    orofaringe = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_examen_estomatognatico,
        verbose_name="Orofaringe",
    )
    atm = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_examen_estomatognatico,
        verbose_name="A.T.M.",
    )
    ganglios = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        choices=paciente_examen_estomatognatico,
        verbose_name="Ganglios",
    )

    def __str__(self):
        return str(self.paciente)


class Cita(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    patient = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    objet = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.patient)

    # class Meta:
    #     ordering = ["-date", "heure"]

    # def ultimasCitas(self):
    #     return self.date >= timezone.now() - datetime.timedelta(days=1)
