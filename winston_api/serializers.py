from rest_framework import serializers

from .models import *


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        partial = True
