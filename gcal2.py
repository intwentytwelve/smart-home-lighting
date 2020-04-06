from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauth2client.service_account import ServiceAccountCredentials
import socketserver
import http.server
import oauth2client.tools
import googleapiclient.sample_tools
from calendar_api.calendar_api import google_calendar_api
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
from phue import Bridge
from pygame import mixer
import time

b = Bridge('192.168.0.13')
b.connect()
b.get_api()

lights = b.lights

# Print light names

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
#    m = google_calender_api()
    lightningLights = ["Haustür", "Keller", "Flurlampe", "Küchenfenster", "Femie", "Stehlampe"]

    def allLightsOn():
        for l in lightningLights:
            b.set_light(1, 'on', True)

    def allLightsOff():
        for l in lightningLights:
            b.set_light(1, 'on', False)

    def allLightsBrightness(brightness):
        for l in lightningLights:
            b.set_light(1, 'bri', brightness)

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/Users/behzadlashgari/Downloads/client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])


    '''
    
    if google_calendar_api.event == True:
        allLightsOn()

        allLightsBrightness(250)
        allLightsBrightness(0)
        time.sleep(.7)
        allLightsBrightness(250)
        allLightsBrightness(0)
        time.sleep(.7)
        allLightsBrightness(250)
        allLightsBrightness(0)
        time.sleep(.7)
        allLightsOff()
        time.sleep(1200)

    '''
    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])
            print(label[INBOX])



if __name__ == '__main__':
    main()

