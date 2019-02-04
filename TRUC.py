   ________                          __     _    __              __     
  / ____/ /__  ____ ___  ___  ____  / /_   | |  / /__  _________/ /___ _
 / /   / / _ \/ __ `__ \/ _ \/ __ \/ __/   | | / / _ \/ ___/ __  / __ `/
/ /___/ /  __/ / / / / /  __/ / / / /_     | |/ /  __/ /  / /_/ / /_/ / 
\____/_/\___/_/ /_/ /_/\___/_/ /_/\__/     |___/\___/_/   \__,_/\__,_/  
                                                                

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

#CE PROGRAMME PERMET L'ENVOI DES ENVENEMENTS VERS GOOGLE AGENDA

def envoi(titre,salle,description,date,date_2):
    #print("INITIALISATION ENVOI")
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=
    [tools.argparser]).parse_args()
    except ImportError:
        flags = None

    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', 
    SCOPES)
        creds = tools.run_flow(flow, store, flags) \
              if flags else tools.run(flow, store)
    CAL = build('calendar', 'v3', http=creds.authorize(Http()))

    print("DEBUT D'ENVOI")
    GMT_OFF = '+01:00'          # ET/MST/GMT-4
    EVENT = {
        'summary': titre,
        'location': salle,
        'description': description,
        'start': {'dateTime': date % GMT_OFF},
        'end': {'dateTime': date_2 % GMT_OFF},
    }

    e = CAL.events().insert(calendarId='primary',
                            sendNotifications=True, body=EVENT).execute()
    print("ENVOI TERMINE")

    print('''*** %r event added:
        Start: %s
        End: %s''' % (e['summary'].encode('utf-8'),
                      e['start']['dateTime'], e['end']['dateTime']))