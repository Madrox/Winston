from __future__ import unicode_literals

from django.db import models


class Package(models.Model):
    message_id = models.CharField(max_length=25, primary_key=True)
    thread_id = models.CharField(max_length=25)
    arrive_datetime = models.DateTimeField(auto_now_add=True)
    picked_up = models.BooleanField(default=False)
