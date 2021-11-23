from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from the_eye import views

urlpatterns = [
    path('rawevents/<int:pk>/', views.EventDetail.as_view()),
    path('rawevents/', views.EventList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
