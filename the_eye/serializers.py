from rest_framework import serializers
from the_eye.models import RawEventsData, Events, Errors


class RawEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawEventsData
        fields = ['id', 'timestamp', 'data']


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['application', 'session_id', 'category', 'data', 'timestamp']


class ErrorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Errors
        fields = ['error_description']
