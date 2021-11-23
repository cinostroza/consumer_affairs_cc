from the_eye.models import RawEventsData, Events, Errors
from the_eye.serializers import RawEventSerializer, EventsSerializer, ErrorsSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


# TODO: Add authentications
# TODO: Add specific views to query Events based on sessions, event types, timestamps etc..

class RawEventViewSet(viewsets.ModelViewSet):
    queryset = RawEventsData.objects.all()
    serializer_class = RawEventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class ErrorViewSet(viewsets.ModelViewSet):
    queryset = Errors.objects.all()
    serializer_class = ErrorsSerializer
