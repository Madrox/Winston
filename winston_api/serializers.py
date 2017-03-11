from rest_framework import serializers

from .models import *


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"


class EventSerializer(serializers.HyperlinkedModelSerializer):
    source = SourceSerializer()

    class Meta:
        model = Event
        fields = "__all__"
        depth = 2
        partial = True
