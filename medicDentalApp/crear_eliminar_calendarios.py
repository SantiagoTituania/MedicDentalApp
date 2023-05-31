from pprint import pprint
from Google import *
import os
from Google import Create_Service, convert_to_RFC_datetime


CLIENT_SECRET_FILE = "credenciales.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# # crear un nuevo calendario En Google Calendar
# request_body = {"summary": "Citas Odontologicas "}
# response = service.calendars().insert(body=request_body).execute()
# print(response)

# # fin de crear un nuevo calendario En Google Calendar

# eliminar un calendario en Google Calendar
# service.calendars().delete(calendarId = "eqcsu76sqgb9ovl23355osjjpo@group.calendar.google.com").execute()

calendar_id = "bvgb2ekb6aeonrrctciumketn4@group.calendar.google.com"

# """
# Crear un event
# """
# colors = service.colors().get().execute()
# pprint(colors)


hora = +5
events = {
    "start": {
        "dateTime": convert_to_RFC_datetime(2023, 5, 6, 11 + hora, 00),
        "timeZone": "America/Guayaquil",
    },
    "end": {
        "dateTime": convert_to_RFC_datetime(2023, 5, 6, 11 + hora, 30),
        "timeZone": "America/Guayaquil",
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
            "title": "LOGO MEDIC DENTAL",
        }
    ],
    "attendees": [
        {
            "comment": "Tienes una nueva cita agendada en Medic Dental",
            "email": "santiago.tituania93@gmail.com",
            "responseStatus": "accepted",
        }
    ],
}

maxAttendees = 5
sendNotification = True
sendUpdate = "none"
supportsAttachments = True

response = (
    service.events()
    .insert(
        calendarId=calendar_id,
        maxAttendees=maxAttendees,
        sendNotifications=sendNotification,
        sendUpdates=sendUpdate,
        supportsAttachments=supportsAttachments,
        body=events,
    )
    .execute()
)

pprint(response)

eventId = response["id"]
