import requests
import json
from os import system
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.dateparse import parse_datetime
from traceback import print_exc


class Command(BaseCommand):
    help = 'Check for anything to say'

    token = '32c9bd7fc2d050e8b2b8194aa2a29fdbf2301ca7'
    # not a real secret calm down
    base_url = 'http://localhost:8000'
    base_path = '/api/events'

    def mark_as_said(self, event):
        r = requests.put(
            event['url'],
            headers={
                "Authorization": "Token %s" % self.token
            },
            data={
                # 'source': event['source']['url'],
                'message': event['message'],
                # 'scheduled_time': event['scheduled_time'],
                'announced': True
            }
        )
        print r.text

    def handle(self, *args, **options):
        r = requests.get(
            self.base_url+self.base_path,
            headers={
                "Authorization": "Token %s" % self.token
            })
        events = json.loads(r.text)
        for event in events:
            dt = parse_datetime(event['scheduled_time'])
            if dt <= datetime.now():
                print "Saying '%s'" % (event['message'])
                system('say -v Daniel %s' % event['message'])
                self.mark_as_said(event)
        print "Done!"
