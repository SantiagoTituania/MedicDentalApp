from django.contrib import admin

# from Google import Create_Service, convert_to_RFC_datetime
from .models import Cita, Enfermedad, Historia, Paciente, Usuario


# Register your models here.
class PacienteAdmin(admin.ModelAdmin):
    list_patient = "nombres"
    search_fields = ["nombres"]


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Usuario)
admin.site.register(Historia)
admin.site.register(Enfermedad)
admin.site.register(Cita)
