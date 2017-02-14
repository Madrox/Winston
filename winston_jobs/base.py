import models
from winston_api.models import Event, Source
from django.utils.timezone import now, localtime


class Job(object):
    def _type(self):
        return self.__class__.__name__

    def make_event(self, msg, when=now()):
        source, created = Source.objects.get_or_create(
            name=self._type()
        )
        Event.objects.create(
            source=source,
            message=msg,
            scheduled_time=localtime(when)
        )

    def __init__(self):
        self.job_model, created = models.Job.objects.get_or_create(
            name=self._type()
        )
        self.history = list()
        self.keys = dict()
        if not created:
            self.history = models.History.objects.filter(
                job=self.job_model
            )
            for keyval in models.KeyVal.objects.filter(job=self.job_model):
                self.keys[keyval.key] = keyval.val

    def val(self, key):
        return self.keys.get(key)

    def set_val(self, key, val):
        keyval, created = models.KeyVal.objects.get_or_create(
            job=self.job_model,
            key=key,
            defaults={
                'val': val
            }
        )
        if not created:
            keyval.val = val
            keyval.save()
        self.keys[key] = keyval.val

    def run(self):
        "Do stuff"
        print "Overload the run method!"
