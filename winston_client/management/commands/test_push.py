import requests
import json
from os import system
from datetime import datetime
from traceback import print_exc

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from lmnotify import LaMetricManager, Model, SimpleFrame, Sound


class Command(BaseCommand):
    help = 'Test LaMetric push'

    client_id = settings.LAMETRIC_CLIENT_ID
    secret = settings.LAMETRIC_SECRET

    def add_arguments(self, parser):
        parser.add_argument(
            '--msg', nargs='?', type=str, default='Hello world!')

    def handle(self, *args, **options):
        # set your LaMetric API credentials here!
        # create an instance of the LaMetricManager
        lmn = LaMetricManager(
            client_id=self.client_id,
            client_secret=self.secret
        )

        # get the LaMetric devices
        devices = lmn.get_devices()

        # use the first device to do some tests
        lmn.set_device(devices[0])

        # prepare a simple frame with an icon and some text
        sf = SimpleFrame("i210", options['msg'])

        # prepare the model that will be send as notification
        model = Model(frames=[sf])
        model.sound = Sound("notifications", "notification3")

        # send the notification the device
        lmn.send_notification(model)
