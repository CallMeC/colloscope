from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import quickstart
import TRUC
import time

#MODIFIEZ ICI VOTRE NUMERO DE GROUPE
groupe = 10


def envoi(titre,salle,description,date,date_2):
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
        flow = client.flow_from_clientsecrets('credentials.json', 
    SCOPES)
        creds = tools.run_flow(flow, store, flags) \
              if flags else tools.run(flow, store)
    CAL = build('calendar', 'v3', http=creds.authorize(Http()))
    GMT_OFF = '+01:00'          # ET/MST/GMT-4
    EVENT = {
        'summary': titre,
        'location': salle,
        'description': description,
        'start': {'dateTime': date % GMT_OFF},
        'end': {'dateTime': date_2 % GMT_OFF},
    }
    time.sleep(1)
    e = CAL.events().insert(calendarId='primary',
                            sendNotifications=True, body=EVENT).execute()
    time.sleep(1)
    print('''*** %r event added:
        Start: %s
        End: %s''' % (e['summary'].encode('utf-8'),
                      e['start']['dateTime'], e['end']['dateTime']))
with open('logs.txt','r+') as f:
	machin = f.readlines()
	if machin == 'False':
		machin = str(input("Entrez votre groupe :",))
		envoi('Configuration','Residence Allix',"Ceci est un test d'envoi",'2019-02-10T13:00:00%s','2019-02-10T14:00:00%s')
		time.sleep(1)
	else:
		f.write('True')
quickstart.export(groupe)