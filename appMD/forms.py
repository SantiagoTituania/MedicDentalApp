from django import forms
from .models import Paciente
from.models import Usuario
from.models import Historia
from.models import Enfermedad


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = '__all__'

class EnfermedadForm(forms.ModelForm):
    class Meta:
        model = Enfermedad
        fields = '__all__'

class CitaForm(forms.Form):
    date = forms.DateField(label="Date")
    heure = forms.TimeField(label='Heure')
    patient = forms.ModelChoiceField(queryset=Paciente.objects.all())
    objet = forms.CharField(label="Objet",max_length=255 ,min_length=1, required=False)

class SearchForm(forms.Form):
    date = forms.DateField(label="Date",required=False)
    patient = forms.ModelChoiceField(queryset=Paciente.objects.all(),required=False)