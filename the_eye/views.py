from the_eye.models import Events
from the_eye.serializers import EventSerializer
from rest_framework import generics


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
