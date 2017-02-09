from __future__ import unicode_literals

from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=100, unique=True)


class History(models.Model):
    job = models.ForeignKey(Job)
    run_date = models.DateTimeField(auto_now_add=True)


class KeyVal(models.Model):
    job = models.ForeignKey(Job)
    key = models.CharField(max_length=100)
    val = models.TextField(blank=True)

    class Meta:
        unique_together = ('job', 'key')
