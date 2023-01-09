"""Widget for Chrome to operate with your Google Calendar"""
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from pprint import pprint
from datetime import datetime, timedelta


scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
#credentials = flow.run_console()
#pickle.dump(credentials, open("token.pkl", "wb"))

credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)


def getCalendar(service):
    """Get the needed calendar and return it's instance."""
    calendarList = service.calendarList().list().execute()

    return calendarList['items'][2]


def getLastCalendarEvent(service):
    """Get the last created event from the calendar."""
    calendarId = getCalendar(service=service)['id']
    result = service.events().list(calendarId=calendarId).execute()

    return result['items'][-1]


def createEvent(service):
    """Create a new certain event."""
    start_time = datetime(2023, 1, 9, 20, 00, 0)
    end_time = start_time + timedelta(hours=4)
    timezone = 'Europe/Kyiv'

    event = {
        'summary': 'Falmer Invasion',
        'location': 'Skyrim/Morfall',
        'description': 'New invasion of falmer race with their new king Joug-Tremae',
        'start': {
                'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': timezone,
            },
        'end': {
                'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': timezone,
            },
        'reminders': {
            'useDefault': False,
            'overrides': [
                    {'method': 'email', 'minutes': 0.5 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

    service.events().insert(calendarId=getCalendar(service=service)['id'], body=event).execute()


def deleteEvent(service):
    """Delete the last created event."""
    service.events().delete(calendarId=getCalendar(service=service)['id'], eventId=getLastCalendarEvent(service=service)["id"]).execute()


def test(service):
    deleteEvent(service)
    pprint(getLastCalendarEvent(service=service))
    deleteEvent(service)
    pprint(getLastCalendarEvent(service=service))


if __name__ == "__main__":
    test(service)