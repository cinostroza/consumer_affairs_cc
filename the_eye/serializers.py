from rest_framework import serializers
from the_eye.models import Events


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['session_id', 'category', 'name', 'data', 'timestamp']
