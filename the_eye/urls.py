from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from the_eye import views

urlpatterns = [
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('events/', views.EventList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)