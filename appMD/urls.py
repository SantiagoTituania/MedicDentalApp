from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicioPaciente, name="inicioPaciente"),
    path("citas/consultarCita", views.consultarCita, name="consultarCita"),
    path("citas/buscarCita", views.buscarCita, name="buscarCita"),
    path(
        "citas/login", LoginView.as_view(template_name="login/login.html"), name="login"
    ),
    path(
        "citas/logout",
        LogoutView.as_view(template_name="logout/login.html"),
        name="logout",
    ),
    path("inicio", views.inicioAdm, name="inicioAdm"),
    path("nosotros", views.nostros, name="nosotros"),
    path("pacientes", views.pacientes, name="pacientes"),
    path("pacientes/registrar", views.registrar, name="registrar"),
    path("pacientes/modificar", views.modificar, name="modificar"),
    path("eliminar/<int:id>", views.eliminar, name="eliminar"),
    path("pacientes/modificar/<int:id>", views.modificar, name="modificar"),
    path("pacientes/buscar", views.buscar, name="buscar"),
    path("usuarios", views.usuarios, name="usuarios"),
    path("usuarios/registrarU", views.registrarU, name="registrarU"),
    path("usuarios/modificarU", views.modificarU, name="modificarU"),
    path("eliminarU/<int:id>", views.eliminarU, name="eliminarU"),
    path("usuarios/modificarU/<int:id>", views.modificarU, name="modificarU"),
    path("usuarios/buscarU", views.buscarU, name="buscarU"),
    path("historiaC", views.historiaC, name="historiaC"),
    # path('historiaClinica/registrarH', views.registrarH, name='registrarH'),
    path("historiaClinica/registrarH", views.registrarH, name="registrarH"),
    path("historiaClinica/modificarH/<int:id>", views.modificarH, name="modificarH"),
    path("historiaClinica/buscarH", views.buscarH, name="buscarH"),
    path("citas/lst", views.lst, name="list"),
    path("citas/suppr/<int:id>/", views.delt, name="delete"),
    path("registrarCita", views.registrarCita, name="registrarCita"),
    path("citas/modif/<int:id>/", views.put, name="put"),
    path("citas/lst/buscarC", views.buscarC, name="buscarC"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
