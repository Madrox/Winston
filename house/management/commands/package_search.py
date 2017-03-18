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


class Command(BaseCommand):
    help = 'Check for packages in gmail'

    def handle(self, *args, **options):
        PackageSearch().as_job()
