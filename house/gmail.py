import requests
import json
from os import system, path
from datetime import datetime
from glob import glob
from importlib import import_module

from django.conf import settings
from django.utils.dateparse import parse_datetime
from traceback import print_exc

from .models import Package


# from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = path.join(
    settings.BASE_DIR,
    'Winston/secrets',
    'gmail_client_secret.json'
)
APPLICATION_NAME = "Winston"


class Gmail(object):
    def get_credentials(self):
        credential_dir = settings.CREDENTIALS_DIR
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'gmail-winston.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            try:
                import argparse
                flags = argparse.ArgumentParser(
                                    parents=[tools.argparser]).parse_args()
            except ImportError:
                flags = None
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            credentials = tools.run_flow(flow, store, None)

        return credentials

    def query(self, query):
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('gmail', 'v1', http=http)

        response = service.users().messages().list(
            userId='me',
            q=query
        ).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(
                userId=user_id,
                q=query,
                pageToken=page_token
            ).execute()
            messages.extend(response['messages'])

        return messages
