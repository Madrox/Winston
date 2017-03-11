from __future__ import unicode_literals

from django.db import models


class Event(models.Model):
    source = models.CharField(max_length=50)
    message = models.TextField()
    scheduled_time = models.DateTimeField(null=True, blank=True)
    speak = models.BooleanField(default=False)
    announced = models.BooleanField(default=False)

    def __unicode__(self):
        return "[%s] %s - %s" % (
                                self.source, self.scheduled_time, self.message)
