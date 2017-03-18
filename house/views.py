import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, View

from .gmail import Gmail
from .models import *


class PackageSearch(View):
    def as_job(self):
        q = "amissionbay@avalonbay.com package"
        for message in Gmail().query(q):
            Package.objects.get_or_create(
                message_id=message['id'],
                thread_id=message['threadId']
            )

    def get(self, request, *args, **kwargs):
        self.as_job()
        return HttpResponse(json.dumps({
            'status': 'success'
        }))


class PackageView(ListView):
    template_name = 'packages.html'
    model = Package


class HomeView(TemplateView):
    template_name = 'home.html'

    package_count = -1

    def packages(self):
        if self.package_count < 0:
            self.package_count = Package.objects.filter(
                picked_up=False
            ).count()
        return self.package_count
