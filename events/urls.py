# # events/urls.py

# from django.urls import path
# from .views import EventListCreateView, EventRetrieveUpdateDestroyView, EventListView

# urlpatterns = [
#     path('events/', EventListCreateView.as_view(), name='event-list-create'),
#     path('events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-detail'),
#     path('events/list/', EventListView.as_view(), name='event-list'),
# ]


# urls.py in events app

from django.urls import path
from .views import EventCreateView

urlpatterns = [
    path('events/create/', EventCreateView.as_view(), name='event-create'),
]
