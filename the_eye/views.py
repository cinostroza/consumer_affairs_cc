from the_eye.models import RawEventsData, Events, Errors
from the_eye.serializers import RawEventSerializer, EventsSerializer, ErrorsSerializer
from rest_framework import viewsets


# TODO: Add authentications

class RawEventViewSet(viewsets.ModelViewSet):
    queryset = RawEventsData.objects.all()
    serializer_class = RawEventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def get_queryset(self):
        queryset = Events.objects.all()
        session = self.request.query_params.get('session')
        event_type = self.request.query_params.get('event_type')
        from_ = self.request.query_params.get('from')
        to_ = self.request.query_params.get('to')

        if session is not None:
            queryset = Events.objects.filter(session_id__exact=session)
        elif event_type is not None:
            queryset = Events.objects.filter(name__exact=event_type)
        elif from_ is not None and to_ is not None:
            queryset = Events.objects.filter(timestamp__range=(from_, to_))
        return queryset


class ErrorViewSet(viewsets.ModelViewSet):
    queryset = Errors.objects.all()
    serializer_class = ErrorsSerializer

    def get_queryset(self):
        queryset = Errors.objects.all()
        app_name = self.request.query_params.get('app_name')
        if app_name is not None:
            queryset = Events.objects.filter(session_id__exact=app_name)
        return queryset
