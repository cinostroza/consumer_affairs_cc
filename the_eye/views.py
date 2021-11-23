from the_eye.models import RawEventsData
from the_eye.serializers import RawEventSerializer
from rest_framework import generics


# TODO: Add authentications
# TODO: Add specific views to query based on sessions, event types, timestamps etc..

class EventList(generics.ListCreateAPIView):
    queryset = RawEventsData.objects.all()
    serializer_class = RawEventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RawEventsData.objects.all()
    serializer_class = RawEventSerializer
