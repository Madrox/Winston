from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.utils.dateparse import parse_datetime

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import *
from .models import *


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(announced=False)
    serializer_class = EventSerializer
    permission_classes = (AllowAny, )


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
