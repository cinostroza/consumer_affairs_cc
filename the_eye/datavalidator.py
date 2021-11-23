from the_eye.models import RawEventsData, Events


# This task should be queued in Celery
# TODO: Create the validator
def data_validator():
    raw_data = RawEventsData.objects.all()
    for raw_event in raw_data:
        # validate the data and once validated save it to the Events table and delete the RawEvent
        pass
