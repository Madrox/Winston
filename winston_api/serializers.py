from rest_framework import serializers

from .models import *


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        depth = 2
        partial = True


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"
