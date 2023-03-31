from django.contrib import admin
from .models import Paciente
from .models import Usuario
from .models import Historia
from .models import Enfermedad
# from Google import Create_Service, convert_to_RFC_datetime
from .models import Cita

# Register your models here.


admin.site.register(Paciente)
admin.site.register(Usuario)
admin.site.register(Historia)
admin.site.register(Enfermedad)
admin.site.register(Cita)


