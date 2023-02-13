from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Paciente
from .forms import PacienteForm
from .models import Usuario
from .forms import UsuarioForm
from .models import Historia
from .forms import HistoriaForm
from .models import Enfermedad
from .forms import EnfermedadForm



from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET,require_http_methods
from .models import Cita
from .forms import CitaForm, SearchForm
from datetime import date
from django.http import Http404
from django.contrib.auth.decorators import login_required



import pickle
import os
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
import datetime


CLIENT_SECRET_FILE = "credenciales.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Create your views here.
def inicioPaciente(request):
    return render(request, 'login/inicioPaciente.html')

def login(request):
    return render(request, 'login/loginUser.html')

def consultarCita(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            form.data = form.cleaned_data
            print(form.cleaned_data)
            if (form.cleaned_data["date"] and form.cleaned_data["patient"]):
                citas = Cita.objects.filter(date=form.cleaned_data["date"] ,patient_icontains=form.cleaned_data["patient"])
            elif (form.cleaned_data["date"] and not form.cleaned_data["patient"]):
                citas = Cita.objects.filter(date=form.cleaned_data["date"])
            elif (not form.cleaned_data["date"] and form.cleaned_data["patient"]):
                citas = Cita.objects.filter(patient_icontains=form.cleaned_data["patient"])
            else: citas = Cita.objects.all()
    else:
        if request.path == '/' :
            citas = Cita.objects.filter(date=date.today())
            form = SearchForm({"date" : date.today()})
        else:    
            form = SearchForm()
            citas = Cita.objects.all()
    return render(request,"login/consultarCita.html", {"citas" : citas, "form": form})  

def buscarCita(request):
    citas = Cita.objects.all()
    buscarCita = request.GET["buscarCita"]
    citas = Cita.objects.filter(patient__icontains=buscarCita)
    context = {'citas': citas}
    return render(request, 'login/consultarCita.html', context) # busca

# @login_required
def inicioAdm(request):
   # return HttpResponse("<h1> Bienvenido a la Clinica Medic Dental</h1>") #imprime un texto html con etiquetas
   return render(request, 'paginas/inicioAdm.html') # busca un archivo .html
def nostros(request):
    return render(request, 'paginas/nosotros.html') # busca un archivo .html

# Accesos a operaciones de pacientes
def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/index.html', {'pacientes': pacientes}) # busca un archivo .html

def registrar(request):
    formulario = PacienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('pacientes')
    return render(request, 'pacientes/registrar.html',{'formulario': formulario}) # busca un archivo .html

def modificar(request, id):
    paciente = Paciente.objects.get(id=id)
    formulario = PacienteForm(request.POST or None, request.FILES or None,instance=paciente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('pacientes')
    return render(request, 'pacientes/modificar.html', {'formulario': formulario}) # busca un archivo .html

def eliminar(request, id):
    paciente = Paciente.objects.get(id=id)
    paciente.delete()
    return redirect('pacientes')

def buscar(request):
    pacientes = Paciente.objects.all()
    buscarPaciente = request.GET["buscarPaciente"]
    pacientes = Paciente.objects.filter(nombres__icontains=buscarPaciente)
    context = {'pacientes': pacientes}
    return render(request, 'pacientes/index.html', context) # busca


    # Accesos a operaciones de usuarios
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/indexUsuarios.html', {'usuarios': usuarios}) # busca un archivo .html

def registrarU(request):
    formularioU = UsuarioForm(request.POST or None, request.FILES or None)
    if formularioU.is_valid():
        formularioU.save()
        return redirect('usuarios')
    return render(request, 'usuarios/registrarUsuarios.html',{'formularioU': formularioU}) # busca un archivo .html

def modificarU(request, id):
    usuario = Usuario.objects.get(id=id)
    formularioU = UsuarioForm(request.POST or None, request.FILES or None,instance=usuario)
    if formularioU.is_valid() and request.POST:
        formularioU.save()
        return redirect('usuarios')
    return render(request, 'usuarios/modificarUsuarios.html', {'formularioU': formularioU}) # busca un archivo .html

def eliminarU(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('usuarios')

def buscarU(request):
    usuarios = Usuario.objects.all()
    buscarUsuario = request.GET["buscarUsuario"]
    usuarios = Usuario.objects.filter(nombres__icontains=buscarUsuario)
    context = {'usuarios': usuarios}
    return render(request, 'usuarios/indexUsuarios.html', context) # busca

    # Accesos a operaciones de pacientes
def historiaC(request):
    historias = Historia.objects.all()
    return render(request, 'historiaClinica/indexHistoriaC.html', {'historias': historias}) # busca un archivo .html

# def registrarH(request):
    formularioH = HistoriaForm(request.POST or None, request.FILES or None)
    if formularioH.is_valid():
        formularioH.save()
        return redirect('historiaC')
    return render(request, 'historiaClinica/registrarHistoriaC.html',{'formularioH': formularioH}) # busca un archivo .html
def registrarH(request):
    formularioH = HistoriaForm(request.POST or None, request.FILES or None)
    if formularioH.is_valid():
        formularioH.save()
        return redirect('historiaC')
    return render(request, 'historiaClinica/registrarHistoriaC.html',{'formularioH': formularioH}) # busca un archivo .html

def enfermedades(request):
    enfermedades = Enfermedad.objects.all()
    return render(request, 'historiaClinica/indexHistoriaC.html', {'enfermedades': enfermedades}) # busca un archivo .html

def enfermedad(request):
    formularioE = EnfermedadForm(request.POST or None, request.FILES or None)
    if formularioE.is_valid():
        formularioE.save()
        return redirect('historiaC')
    return render(request, 'historiaClinica/registrarHistoriaC.html',{'formularioE': formularioE}) # busca un archivo .html



def buscarH(request):
    historias = Historia.objects.all()
    buscarHistoria = request.GET["buscarHistoria"]
    historias = Historia.objects.filter(id__icontains=buscarHistoria)
    context = {'historias': historias}
    return render(request, 'historiaClinica/indexHistoriaC.html', context) # busca

class HistoriaListView(ListView):
    model = Historia, Enfermedad
    template_name = 'historiaClinica/indexHistoriaC.html'


# @login_required
@require_http_methods(["GET","POST"])
def lst(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            form.data = form.cleaned_data
            print(form.cleaned_data)
            if (form.cleaned_data["date"] and form.cleaned_data["patient"]):
                citas = Cita.objects.filter(date=form.cleaned_data["date"] ,patient=form.cleaned_data["patient"])
            elif (form.cleaned_data["date"] and not form.cleaned_data["patient"]):
                citas = Cita.objects.filter(date=form.cleaned_data["date"])
            elif (not form.cleaned_data["date"] and form.cleaned_data["patient"]):
                citas = Cita.objects.filter(patient=form.cleaned_data["patient"])
            else: citas = Cita.objects.all()
    else:
        if request.path == '/' :
            citas = Cita.objects.filter(date=date.today())
            form = SearchForm({"date" : date.today()})
        else:    
            form = SearchForm()
            citas = Cita.objects.all()
    return render(request,"citas/list.html", {"citas" : citas, "form": form})

# @login_required
@require_GET
def detail(request,id):
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
@require_http_methods(["GET","POST"])
def registrarCita(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data["date"]
            heure = form.cleaned_data["heure"]
            patient = form.cleaned_data["patient"]
            objet = form.cleaned_data["objet"]
            r = Cita(date=date, heure=heure, patient=patient, objet=objet)
            r.save()
            #cita
            
            return HttpResponseRedirect("/citas/lst")
            events()
    else:
        form = CitaForm()
    return render(request,"citas/registrarCita.html", {"form": form})


# @login_required
@require_http_methods(["GET","POST"])
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
    return render(request,"citas/modif.html", {"form" : form, "id" : r.id})

service = (CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
calendar_id = 'eqcsu76sqgb9ovl23355osjjpo@group.calendar.google.com'
events = {
     'start': {
         "dateTime": (2023, 2, 7, 19,45 ),
         "timeZone": "America/Guayaquil"
     },
     "end": {
         "dateTime":(2023, 2, 7, 20, 45 ),
         "timeZone": "America/Guayaquil"
     },
    "summary": "Cita Medic Dental",
    "description": "Control Mensual",
    "colorId": 2,
    "status": "confirmed",
    "visibility": "private",
    "location": "Ecuador",
    "attachments": [
        {
            "fileUrl": "https://drive.google.com/file/d/1ancKy-4tYqRiG0xm8ELqiJE5XPmz63Ih/view?usp=share_link",
            "title": "LOGO MEDIC DENTAL"
        }
    ],
    "attendees": [
        {
            "comment": "Tienes una nueva cita agendada en Medic Dental",
            "email": "santiago.tituania93@gmail.com",
            "responseStatus": "accepted"
        }
    
    ],
   }

maxAttendees = 5
sendNotification = True
sendUpdate = "none"
supportsAttachments = True
def event(request):
    response = service.events().insert(
    calendarId = calendar_id,
    maxAttendees = maxAttendees,
    sendNotifications = sendNotification,
    sendUpdates = sendUpdate,
    supportsAttachments = supportsAttachments,
    body = events

).execute()


def Create_Service(client_secret_file, api_name, api_version, *scopes):
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    print(SCOPES)

    cred = None

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    # print(pickle_file)

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None

def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt
