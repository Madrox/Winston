import requests
import json
from os import system
from datetime import datetime
from traceback import print_exc

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from django.conf import settings

from lmnotify import LaMetricManager, Model, SimpleFrame, Sound

from winston_client import speech


class Command(BaseCommand):
    help = 'Check for anything to say'

    client_id = settings.LAMETRIC_CLIENT_ID
    secret = settings.LAMETRIC_SECRET

    token = settings.WINSTON_API_TOKEN
    # not a real secret calm down
    base_url = settings.WINSTON_API_DOMAIN
    base_path = '/api/events'

    def push_message(self, msg):
        lmn = LaMetricManager(
            client_id=self.client_id,
            client_secret=self.secret
        )

        # get the LaMetric devices
        devices = lmn.get_devices()

        # use the first device to do some tests
        lmn.set_device(devices[0])

        # prepare a simple frame with an icon and some text
        sf = SimpleFrame("i210", msg)

        # prepare the model that will be send as notification
        model = Model(frames=[sf])
        model.sound = Sound("notifications", "notification3")

        # send the notification the device
        lmn.send_notification(model)

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

    def push_speech(self, msg):
        s = speech.Speech()
        print "Saying '%s'" % (msg)
        # system('say -v Daniel %s' % event['message'])
        s.make("<speak>%s</speak>" % (msg))
        s.chime()
        s.say("<speak>%s</speak>" % (msg))

    def handle(self, *args, **options):
        r = requests.get(
            self.base_url+self.base_path,
            headers={
                "Authorization": "Token %s" % self.token
            })
        events = json.loads(r.text)
        for event in events:
            dt = event['scheduled_time']
            if dt is not None:
                dt = parse_datetime(event['scheduled_time'])
            if dt is None or dt <= make_aware(datetime.now()):
                if event['speak']:
                    self.push_speech(event['message'])
                    self.mark_as_said(event)
                else:
                    self.push_message(event['message'])
        print "Done!"
