from the_eye.models import Events
from the_eye.serializers import EventSerializer
from rest_framework import generics


# TODO: Add authentications
# TODO: Add specific views to query based on sessions, event types, timestamps etc..

class EventList(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
