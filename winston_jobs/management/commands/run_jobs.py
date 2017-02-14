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

from winston_jobs.base import Job


class Command(BaseCommand):
    help = 'Check for anything to say'

    def handle(self, *args, **options):
        file_path = path.join(path.dirname(path.abspath(__file__)))
        files = glob(file_path + "/../../jobs/*.py")
        for f in files:
            name = path.splitext(path.basename(f))[0]
            # add package prefix to name, if required
            package = "winston_jobs.jobs.%s" % (name)
            module = import_module(package)
            for member in dir(module):
                if member.startswith("__"):
                    continue
                submodule = getattr(module, member)
                try:
                    if issubclass(submodule, Job) and submodule is not Job:
                        job = submodule()
                        job.run()
                except TypeError:
                    pass
