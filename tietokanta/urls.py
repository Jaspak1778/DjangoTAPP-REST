from django.urls import path
from .views import EventListCreateAPI, EventDetailAPI

urlpatterns = [
    path('events/', EventListCreateAPI.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailAPI.as_view(), name='event-detail'),
]