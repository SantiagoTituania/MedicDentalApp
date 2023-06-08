from django import forms

from .models import Enfermedad, Historia, Paciente, Usuario


class PacienteForm(forms.ModelForm):
    # SEXO_CHOICES = [
    #     ('M', 'Masculino'),
    #     ('F', 'Femenino')
    # ]

    # sexo = forms.CharField(
    #     widget=forms.Select(choices=SEXO_CHOICES)
    # )
    class Meta:
        model = Paciente
        fields = "__all__"


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"


class HistoriaForm(forms.Form):
    paciente_enfermedad = [("S", "Si"), ("N", "No")]
    paciente = forms.ModelChoiceField(queryset=Paciente.objects.all())
    motivoConsulta = forms.CharField(
        max_length=11, label="Motivo Consulta", required=False
    )
    antibioticosAlergia = forms.CharField(
        max_length=11, label="Alergia antibióticos", required=False
    )
    anestesiaAlergia = forms.CharField(
        max_length=11, label="Alergia anestesia", required=False
    )
    hemorragias = forms.ModelChoiceField(
        queryset=Historia.objects.all(), required=False
    )
    sida = forms.CharField(max_length=11, label="VIH/SIDA", required=False)
    tuberculosis = forms.CharField(max_length=11, label="Tuberculosis", required=False)
    asma = forms.CharField(max_length=11, label="Asma", required=False)
    diabetes = forms.CharField(max_length=11, label="Diabetes", required=False)
    hipertension = forms.CharField(max_length=11, label="Hipertensión", required=False)
    cardiacas = forms.CharField(
        max_length=11, label="Enfermedad cardiacas", required=False
    )
    otros = forms.CharField(max_length=200, label="Otros", required=False)

    fechaTratamiento1 = forms.DateField(label="Fecha Tratamiento 1", required=False)
    desTratamiento1 = forms.CharField(
        max_length=200, label="Descripción Tratamiento 1", required=False
    )
    fechaTratamiento2 = forms.DateField(label="Fecha Tratamiento 2", required=False)
    desTratamiento2 = forms.CharField(
        max_length=200, label="Descripción Tratamiento 2", required=False
    )
    fechaTratamiento3 = forms.DateField(label="Fecha Tratamiento 3", required=False)
    desTratamiento3 = forms.CharField(
        max_length=200, label="Descripción Tratamiento 3", required=False
    )
    fechaTratamiento4 = forms.DateField(label="Fecha Tratamiento 4", required=False)
    desTratamiento4 = forms.CharField(
        max_length=200, label="Descripción Tratamiento 4", required=False
    )
    # fechaTratamiento5 = forms.DateField(label="Fecha Tratamiento 5", required=False)
    # desTratamiento5 = forms.CharField(
    #     max_length=200, label="Descripción Tratamiento 5", required=False
    # )
    # fechaTratamiento6 = forms.DateField(label="Fecha Tratamiento 6", required=False)
    # desTratamiento6 = forms.CharField(
    #     max_length=200, label="Descripción Tratamiento 6", required=False
    # )
    # fechaTratamiento7 = forms.DateField(label="Fecha Tratamiento 7", required=False)
    # desTratamiento7 = forms.CharField(
    #     max_length=200, label="Descripción Tratamiento 7", required=False
    # )
    # fechaTratamiento8 = forms.DateField(label="Fecha Tratamiento 8", required=False)
    # desTratamiento8 = forms.CharField(
    #     max_length=200, label="Descripción Tratamiento 8", required=False
    # )
    # fechaTratamiento9 = forms.DateField(label="Fecha Tratamiento 9", required=False)
    # desTratamiento9 = forms.CharField(
    #     max_length=200, label="Descripción Tratamiento 9", required=False
    # )
    # fechaTratamiento10 = forms.DateField(label="Fecha Tratamiento 10", required=False)
    # desTratamiento10 = forms.CharField(
    #     max_length=200, label="Descripción Tratamiento 10", required=False
    # )
    # fechaTratamiento11 = forms.DateField(label="Fecha Tratamiento 11", required=False)
    # desTratamiento11 = forms.CharField(
    #     max_length=200, label="Descripción Tratamiento 11", required=False
    # )
    # fechaTratamiento12 = forms.DateField(label="Fecha Tratamiento 12", required=False)
    # desTratamiento12 = forms.CharField(
    #     max_length=200, label="Descripción Tratamiento 12", required=False
    # )
    presionArterial = forms.CharField(
        max_length=10, label="Presión Arterial", required=False
    )
    frecuenciaCardiaca = forms.CharField(
        max_length=10, label="Frecuencia Cardiaca", required=False
    )
    temperatura = forms.CharField(max_length=10, label="Temperatura", required=False)
    frecuenciaRespiratoria = forms.CharField(
        max_length=10, label="Frecuencia respiratoria", required=False
    )
    labios = forms.CharField(max_length=11, label="Labios", required=False)
    mejillas = forms.CharField(max_length=11, label="Mejillas", required=False)
    maxilarSuperior = forms.CharField(
        max_length=11, label="Maxilar Superior", required=False
    )
    maxilarInferior = forms.CharField(
        max_length=11, label="Maxilar Inferior", required=False
    )
    lengua = forms.CharField(max_length=11, label="Lengua", required=False)
    paladar = forms.CharField(max_length=11, label="Paladar", required=False)
    piso = forms.CharField(max_length=11, label="Piso", required=False)
    carrillo = forms.CharField(max_length=11, label="Carrillo", required=False)
    glandulasSalivales = forms.CharField(
        max_length=11, label="Glándulas Salivales", required=False
    )
    orofaringe = forms.CharField(max_length=11, label="Orofaringe", required=False)
    atm = forms.CharField(max_length=11, label="A.T.M.", required=False)
    ganglios = forms.CharField(max_length=11, label="Ganglios", required=False)


class EnfermedadForm(forms.ModelForm):
    class Meta:
        model = Enfermedad
        fields = "__all__"


class CitaForm(forms.Form):
    date = forms.DateField(label="Date")
    heure = forms.TimeField(label="Heure")
    patient = forms.ModelChoiceField(queryset=Paciente.objects.all())
    objet = forms.CharField(label="Objet", max_length=255, min_length=1, required=False)


class SearchForm(forms.Form):
    date = forms.DateField(label="Date", required=False)
    patient = forms.ModelChoiceField(queryset=Paciente.objects.all(), required=False)
