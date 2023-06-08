import datetime
import os
from datetime import date, timedelta

from apiclient.discovery import build
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods
from django.views.generic import ListView

from .forms import (
    CitaForm,
    EnfermedadForm,
    HistoriaForm,
    PacienteForm,
    SearchForm,
    UsuarioForm,
)
from .Google import Create_Service, convert_to_RFC_datetime
from .models import Cita, Enfermedad, Historia, Paciente, Usuario

CLIENT_SECRET_FILE = "credenciales.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

calendar_id = "bvgb2ekb6aeonrrctciumketn4@group.calendar.google.com"


# Create your views here.
def inicioPaciente(request):
    return render(request, "login/inicioPaciente.html")


def login(request):
    return render(request, "login/login.html")


def consultarCita(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            form.data = form.cleaned_data
            print(form.cleaned_data)
            if form.cleaned_data["date"] and form.cleaned_data["patient"]:
                citas = Cita.objects.filter(
                    date=form.cleaned_data["date"],
                    patient_icontains=form.cleaned_data["patient"],
                )
            elif form.cleaned_data["date"] and not form.cleaned_data["patient"]:
                citas = Cita.objects.filter(date=form.cleaned_data["date"])
            elif not form.cleaned_data["date"] and form.cleaned_data["patient"]:
                citas = Cita.objects.filter(
                    patient_icontains=form.cleaned_data["patient"]
                )
            else:
                citas = Cita.objects.all()
    else:
        if request.path == "/":
            citas = Cita.objects.filter(date=date.today())
            form = SearchForm({"date": date.today()})
        else:
            form = SearchForm()
            citas = Cita.objects.all()
    return render(request, "login/consultarCita.html", {"citas": citas, "form": form})


def buscarCita(request):
    citas = Cita.objects.all()
    buscarCita = request.GET["buscarCita"]
    citas = Cita.objects.filter(patient__icontains=buscarCita)
    context = {"citas": citas}
    return render(request, "login/consultarCita.html", context)  # busca


@login_required
def inicioAdm(request):
    # return HttpResponse("<h1> Bienvenido a la Clinica Medic Dental</h1>") #imprime un texto html con etiquetas
    return render(request, "paginas/inicioAdm.html")  # busca un archivo .html


def nostros(request):
    return render(request, "paginas/nosotros.html")  # busca un archivo .html


# Accesos a operaciones de pacientes
@login_required
def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(
        request, "pacientes/index.html", {"pacientes": pacientes}
    )  # busca un archivo .html


@require_http_methods(["GET", "POST"])
def registrar(request):
    if request.method == "POST":
        formp = PacienteForm(request.POST)
        if formp.is_valid():
            nombres = formp.cleaned_data["nombres"]
            apellidos = formp.cleaned_data["apellidos"]
            cedula = formp.cleaned_data["cedula"]
            fechaNacimiento = formp.cleaned_data["fechaNacimiento"]
            sexo = formp.cleaned_data["sexo"]
            direccion = formp.cleaned_data["direccion"]
            celular = formp.cleaned_data["celular"]
            correo = formp.cleaned_data["correo"]
            pac = Paciente(
                nombres=nombres,
                apellidos=apellidos,
                cedula=cedula,
                fechaNacimiento=fechaNacimiento,
                sexo=sexo,
                direccion=direccion,
                celular=celular,
                correo=correo,
            )
            pac.save()
            messages.success(request, "Paciente registrado exitosamente")
            # pacientes

            return redirect("pacientes")
            events()
    else:
        formp = PacienteForm()
    return render(request, "pacientes/registrar.html", {"formp": formp})


# def registrar(request):
#     formulario = PacienteForm(request.POST or None, request.FILES or None)
#     if formulario.is_valid():
#         formulario.save()
#         return redirect('pacientes')
#     return render(request, 'pacientes/registrar.html',{'formulario': formulario}) # busca un archivo .html
@require_http_methods(["GET", "POST"])
def modificar(request, id):
    try:
        pac = Paciente.objects.get(pk=id)
    except Paciente.DoesNotExist:
        raise Http404("El paciente no existe!")
    else:
        if request.method == "POST":
            formp = PacienteForm(
                request.POST or None, request.FILES or None, instance=pac
            )
            if formp.is_valid() and request.POST:
                pac.nombres = formp.cleaned_data["nombres"]
                pac.apellidos = formp.cleaned_data["apellidos"]
                pac.cedula = formp.cleaned_data["cedula"]
                pac.fechaNacimiento = formp.cleaned_data["fechaNacimiento"]
                pac.sexo = formp.cleaned_data["sexo"]
                pac.direccion = formp.cleaned_data["direccion"]
                pac.celular = formp.cleaned_data["celular"]
                pac.correo = formp.cleaned_data["correo"]
                pac.save()
                messages.success(request, "Modificado correctamente")
                return redirect("pacientes")
        else:
            a = {
                "nombres": pac.nombres,
                "apellidos": pac.apellidos,
                "cedula": pac.cedula,
                "fechaNacimiento": pac.fechaNacimiento,
                "sexo": pac.sexo,
                "direccion": pac.direccion,
                "celular": pac.celular,
                "correo": pac.correo,
            }
            formp = PacienteForm(a)
    return render(request, "pacientes/modificar.html", {"formp": formp, "id": pac.id})


def eliminar(request, id):
    paciente = Paciente.objects.get(id=id)
    paciente.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect("pacientes")


def buscar(request):
    pacientes = Paciente.objects.all()
    buscarPaciente = request.GET["buscarPaciente"]
    pacientes = Paciente.objects.filter(nombres__icontains=buscarPaciente)
    context = {"pacientes": pacientes}
    return render(request, "pacientes/index.html", context)  # busca

    # Accesos a operaciones de usuarios


def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(
        request, "usuarios/indexUsuarios.html", {"usuarios": usuarios}
    )  # busca un archivo .html


def registrarU(request):
    formularioU = UsuarioForm(request.POST or None, request.FILES or None)
    if formularioU.is_valid():
        formularioU.save()
        username = formularioU.cleaned_data["nUsuario"]
        messages.success(request, f"Usuario {username} creado")
        return redirect("usuarios")
    return render(
        request, "usuarios/registrarUsuarios.html", {"formularioU": formularioU}
    )  # busca un archivo .html


def modificarU(request, id):
    usuario = Usuario.objects.get(id=id)
    formH = UsuarioForm(request.POST or None, request.FILES or None, instance=usuario)
    if formH.is_valid() and request.POST:
        formH.save()
        return redirect("usuarios")
    return render(
        request, "usuarios/modificarUsuarios.html", {"formH": formH}
    )  # busca un archivo .html


def eliminarU(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect("usuarios")


def buscarU(request):
    usuarios = Usuario.objects.all()
    buscarUsuario = request.GET["buscarUsuario"]
    usuarios = Usuario.objects.filter(nombres__icontains=buscarUsuario)
    context = {"usuarios": usuarios}
    return render(request, "usuarios/indexUsuarios.html", context)  # busca

    # Accesos a operaciones de pacientes


def historiaC(request):
    historias = Historia.objects.all()
    return render(
        request, "historiaClinica/indexHistoriaC.html", {"historias": historias}
    )  # busca un archivo .html


@require_http_methods(["GET", "POST"])
def registrarH(request):
    if request.method == "POST":
        formH = HistoriaForm(request.POST)
        if formH.is_valid():
            paciente = formH.cleaned_data["paciente"]
            motivoConsulta = formH.cleaned_data["motivoConsulta"]
            antibioticosAlergia = formH.cleaned_data["antibioticosAlergia"]
            anestesiaAlergia = formH.cleaned_data["anestesiaAlergia"]
            hemorragias = formH.cleaned_data["hemorragias"]
            sida = formH.cleaned_data["sida"]
            tuberculosis = formH.cleaned_data["tuberculosis"]
            asma = formH.cleaned_data["asma"]
            diabetes = formH.cleaned_data["diabetes"]
            hipertension = formH.cleaned_data["hipertension"]
            cardiacas = formH.cleaned_data["cardiacas"]
            otros = formH.cleaned_data["otros"]
            fechaTratamiento1 = formH.cleaned_data["fechaTratamiento1"]
            desTratamiento1 = formH.cleaned_data["desTratamiento1"]
            fechaTratamiento2 = formH.cleaned_data["fechaTratamiento2"]
            desTratamiento2 = formH.cleaned_data["desTratamiento2"]
            fechaTratamiento3 = formH.cleaned_data["fechaTratamiento3"]
            desTratamiento3 = formH.cleaned_data["desTratamiento3"]
            fechaTratamiento4 = formH.cleaned_data["fechaTratamiento4"]
            desTratamiento4 = formH.cleaned_data["desTratamiento4"]
            presionArterial = formH.cleaned_data["presionArterial"]
            frecuenciaCardiaca = formH.cleaned_data["frecuenciaCardiaca"]
            temperatura = formH.cleaned_data["temperatura"]
            frecuenciaRespiratoria = formH.cleaned_data["frecuenciaRespiratoria"]
            labios = formH.cleaned_data["labios"]
            mejillas = formH.cleaned_data["mejillas"]
            maxilarSuperior = formH.cleaned_data["maxilarSuperior"]
            maxilarInferior = formH.cleaned_data["maxilarInferior"]
            lengua = formH.cleaned_data["lengua"]
            paladar = formH.cleaned_data["paladar"]
            piso = formH.cleaned_data["piso"]
            carrillo = formH.cleaned_data["carrillo"]
            glandulasSalivales = formH.cleaned_data["glandulasSalivales"]
            orofaringe = formH.cleaned_data["orofaringe"]
            atm = formH.cleaned_data["atm"]
            ganglios = formH.cleaned_data["ganglios"]
            h = Historia(
                paciente=paciente,
                motivoConsulta=motivoConsulta,
                antibioticosAlergia=antibioticosAlergia,
                anestesiaAlergia=anestesiaAlergia,
                hemorragias=hemorragias,
                sida=sida,
                tuberculosis=tuberculosis,
                asma=asma,
                diabetes=diabetes,
                hipertension=hipertension,
                cardiacas=cardiacas,
                otros=otros,
                fechaTratamiento1=fechaTratamiento1,
                desTratamiento1=desTratamiento1,
                fechaTratamiento2=fechaTratamiento2,
                desTratamiento2=desTratamiento2,
                fechaTratamiento3=fechaTratamiento3,
                desTratamiento3=desTratamiento3,
                fechaTratamiento4=fechaTratamiento4,
                desTratamiento4=desTratamiento4,
                presionArterial=presionArterial,
                frecuenciaCardiaca=frecuenciaCardiaca,
                temperatura=temperatura,
                frecuenciaRespiratoria=frecuenciaRespiratoria,
                labios=labios,
                mejillas=mejillas,
                maxilarSuperior=maxilarSuperior,
                maxilarInferior=maxilarInferior,
                lengua=lengua,
                paladar=paladar,
                piso=piso,
                carrillo=carrillo,
                glandulasSalivales=glandulasSalivales,
                orofaringe=orofaringe,
                atm=atm,
                ganglios=ganglios,
            )
            h.save()
            return HttpResponseRedirect("/historiaC")
            events()
    else:
        formH = HistoriaForm()
    return render(request, "historiaClinica/registrarHistoriaC.html", {"formH": formH})


def buscarH(request):
    historias = Historia.objects.all()
    buscarHistoria = request.GET["buscarHistoria"]
    historias = Historia.objects.filter(id__icontains=buscarHistoria)
    context = {"historias": historias}
    return render(request, "historiaClinica/indexHistoriaC.html", context)  # busca


@require_http_methods(["GET", "POST"])
def modificarH(request, id):
    try:
        h = Historia.objects.get(pk=id)
    except Historia.DoesNotExist:
        raise Http404("La historia no existe!")
    else:
        if request.method == "POST":
            formH = HistoriaForm(
                request.POST or None, request.FILES or None, instance=h
            )
            if formH.is_valid() and request.POST:
                h.paciente = formH.cleaned_data["paciente"]
                h.motivoConsulta = formH.cleaned_data["motivoConsulta"]
                h.antibioticosAlergia = formH.cleaned_data["antibioticosAlergia"]
                h.anestesiaAlergia = formH.cleaned_data["anestesiaAlergia"]
                h.hemorragias = formH.cleaned_data["hemorragias"]
                h.sida = formH.cleaned_data["sida"]
                h.tuberculosis = formH.cleaned_data["tuberculosis"]
                h.asma = formH.cleaned_data["asma"]
                h.diabetes = formH.cleaned_data["diabetes"]
                h.hipertension = formH.cleaned_data["hipertension"]
                h.cardiacas = formH.cleaned_data["cardiacas"]
                h.otros = formH.cleaned_data["otros"]
                h.fechaTratamiento1 = formH.cleaned_data["fechaTratamiento1"]
                h.desTratamiento1 = formH.cleaned_data["desTratamiento1"]
                h.fechaTratamiento2 = formH.cleaned_data["fechaTratamiento2"]
                h.desTratamiento2 = formH.cleaned_data["desTratamiento2"]
                h.fechaTratamiento3 = formH.cleaned_data["fechaTratamiento3"]
                h.desTratamiento3 = formH.cleaned_data["desTratamiento3"]
                h.fechaTratamiento4 = formH.cleaned_data["fechaTratamiento4"]
                h.desTratamiento4 = formH.cleaned_data["desTratamiento4"]
                h.presionArterial = formH.cleaned_data["presionArterial"]
                h.frecuenciaCardiaca = formH.cleaned_data["frecuenciaCardiaca"]
                h.temperatura = formH.cleaned_data["temperatura"]
                h.frecuenciaRespiratoria = formH.cleaned_data["frecuenciaRespiratoria"]
                h.labios = formH.cleaned_data["labios"]
                h.mejillas = formH.cleaned_data["mejillas"]
                h.maxilarSuperior = formH.cleaned_data["maxilarSuperior"]
                h.maxilarInferior = formH.cleaned_data["maxilarInferior"]
                h.lengua = formH.cleaned_data["lengua"]
                h.paladar = formH.cleaned_data["paladar"]
                h.piso = formH.cleaned_data["piso"]
                h.carrillo = formH.cleaned_data["carrillo"]
                h.glandulasSalivales = formH.cleaned_data["glandulasSalivales"]
                h.orofaringe = formH.cleaned_data["orofaringe"]
                h.atm = formH.cleaned_data["atm"]
                h.ganglios = formH.cleaned_data["ganglios"]
                # messages.success(request, "Modificado correctamente")
                return redirect("/historiaC")
        else:
            hh = {
                "paciente": h.paciente,
                "motivoConsulta": h.motivoConsulta,
                "antibioticosAlergia": h.antibioticosAlergia,
                "anestesiaAlergia": h.anestesiaAlergia,
                "hemorragias": h.hemorragias,
                "sida": h.sida,
                "tuberculosis": h.tuberculosis,
                "asma": h.asma,
                "diabetes": h.diabetes,
                "hipertension": h.hipertension,
                "cardiacas": h.cardiacas,
                "otros": h.otros,
                "fechaTratamiento1": h.fechaTratamiento1,
                "desTratamiento1": h.desTratamiento1,
                "fechaTratamiento2": h.fechaTratamiento2,
                "desTratamiento2": h.desTratamiento2,
                "fechaTratamiento3": h.fechaTratamiento3,
                "desTratamiento3": h.desTratamiento3,
                "fechaTratamiento4": h.fechaTratamiento4,
                "desTratamiento4": h.desTratamiento4,
                "presionArterial": h.presionArterial,
                "frecuenciaCardiaca": h.frecuenciaCardiaca,
                "temperatura": h.temperatura,
                "frecuenciaRespiratoria": h.frecuenciaRespiratoria,
                "labios": h.labios,
                "mejillas": h.mejillas,
                "maxilarSuperior": h.maxilarSuperior,
                "maxilarInferior": h.maxilarInferior,
                "lengua": h.lengua,
                "paladar": h.paladar,
                "piso": h.piso,
                "carrillo": h.carrillo,
                "glandulasSalivales": h.glandulasSalivales,
                "orofaringe": h.orofaringe,
                "atm": h.atm,
                "ganglios": h.ganglios,
            }
            formH = HistoriaForm(hh)
    return render(
        request, "historiaClinica/modificarHistoriaC.html", {"formH": formH, "id": h.id}
    )


def buscarC(request):
    citas = Cita.objects.all()
    buscarCita = request.GET["buscarCita"]
    citas = Cita.objects.filter(id__icontains=buscarCita)
    context = {"citas": citas}
    return render(request, "citas/list.html", {"citas": citas})

    # buscacitas


@login_required
@require_http_methods(["GET", "POST"])
def lst(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            form.data = form.cleaned_data
            print(form.cleaned_data)
            if form.cleaned_data["date"] and form.cleaned_data["patient"]:
                citas = Cita.objects.filter(
                    date=form.cleaned_data["date"], patient=form.cleaned_data["patient"]
                )
            elif form.cleaned_data["date"] and not form.cleaned_data["patient"]:
                citas = Cita.objects.filter(date=form.cleaned_data["date"])
            elif not form.cleaned_data["date"] and form.cleaned_data["patient"]:
                citas = Cita.objects.filter(patient=form.cleaned_data["patient"])
            else:
                citas = Cita.objects.all()
    else:
        if request.path == "/":
            citas = Cita.objects.filter(date=date.today())
            form = SearchForm({"date": date.today()})
        else:
            form = SearchForm()
            citas = Cita.objects.all()
    return render(request, "citas/list.html", {"citas": citas, "form": form})


# @login_required
@require_GET
def detail(request, id):
    try:
        citas = Cita.objects.get(id=id)
    except Cita.DoesNotExist:
        raise Http404("Appointment does not exist")
    return HttpResponse(citas)


# @login_required
@require_GET
def delt(request, id):
    try:
        Cita.objects.get(pk=id).delete()
    except Cita.DoesNotExist:
        raise Http404("Appointment does not exist")
    return HttpResponseRedirect("/citas/lst")


# @login_required
@require_http_methods(["GET", "POST"])
def registrarCita(request):
    # service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data["date"]
            date = request.POST["date"]
            heure = form.cleaned_data["heure"]
            heure = request.POST["heure"]
            patient = form.cleaned_data["patient"]
            objet = form.cleaned_data["objet"]
            objet = request.POST["objet"]
            starts = date + " " + heure + ":" "00"
            start_time = datetime.datetime.strptime(starts, "%Y-%m-%d %H:%M:%S")
            end_time = start_time + timedelta(minutes=30)
            timezone = "America/Guayaquil"

            r = Cita(date=date, heure=heure, patient=patient, objet=objet)
            r.save()
            print("fecha y hora", start_time.isoformat(), "fin", end_time.isoformat())
            print("paciente", patient)
            print("motivo", objet),

            events = (
                service.events()
                .insert(
                    calendarId="primary",
                    body={
                        "summary": "Cita Medic Dental",
                        "start": {
                            "dateTime": start_time.isoformat(),
                            "timeZone": timezone,
                        },
                        "end": {
                            "dateTime": end_time.isoformat(),
                            "timeZone": timezone,
                        },
                        "attendees": [
                            {
                                "comment": "Tienes una nueva cita agendada en Medic Dental",
                                "email": "santiago.tituania93@gmail.com",
                                "responseStatus": "accepted",
                            }
                        ],
                    },
                )
                .execute()
            )
            # cita

            return HttpResponseRedirect("/citas/lst")
            events()
    else:
        form = CitaForm()
    return render(request, "citas/registrarCita.html", {"form": form})


# @login_required
@require_http_methods(["GET", "POST"])
def put(request, id):
    try:
        r = Cita.objects.get(pk=id)
    except Cita.DoesNotExist:
        raise Http404("Appointment does not exist")
    else:
        if request.method == "POST":
            form = CitaForm(request.POST)
            if form.is_valid():
                r.date = form.cleaned_data["date"]
                r.heure = form.cleaned_data["heure"]
                r.patient = form.cleaned_data["patient"]
                r.objet = form.cleaned_data["objet"]
                r.save()
                return HttpResponseRedirect("/citas/lst")
        else:
            q = {
                "date": r.date,
                "heure": r.heure,
                "patient": r.patient,
                "objet": r.objet,
            }
            form = CitaForm(q)
    return render(request, "citas/modif.html", {"form": form, "id": r.id})


scopes = ["https://www.googleapis.com/auth/calendar"]
credentials = "credenciales.json"
