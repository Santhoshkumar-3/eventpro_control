from django.urls import path
from .views import EventCreateView, EventRetrieveUpdateDestroyView, EventListView, EventSearchView

urlpatterns = [
    path('events/create/', EventCreateView.as_view(), name='event-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-detail'),
    path('events/list/', EventListView.as_view(), name='event-list'),
    path('events/search/', EventSearchView.as_view(), name='event-search'),
]
