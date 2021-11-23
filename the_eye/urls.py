from django.urls import path, include
from rest_framework.routers import DefaultRouter
from the_eye import views

router = DefaultRouter()
router.register(r'rawevents', views.RawEventViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'errors', views.ErrorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]