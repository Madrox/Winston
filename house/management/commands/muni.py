import requests
import json
from os import system, path
from datetime import datetime
from glob import glob
from importlib import import_module

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.dateparse import parse_datetime
from traceback import print_exc

from house.views import *

import nextbus
import json


class Command(BaseCommand):
    help = 'Check for packages in gmail'

    def handle(self, *args, **options):
        nb = nextbus.NextBus()

        agency = [a for a in nextbus.agencies() if a.tag == 'sf-muni'].pop()
        route = [r for r in agency.routes if r.tag == 'N'].pop()
        # print route.directions
        for s in route.directions:
            print dir(s)
        schedule = [s for s in route.schedule if s.direction != 'Inbound'].pop()

        print schedule
