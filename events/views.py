# views.py in events app

from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Event
from .serializers import EventSerializer
from users.models import CustomUser

class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if user.role == 'staff':
            serializer.save()
        else:
            raise PermissionDenied("Only staff users can create events.")



class EventSearchView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            return Event.objects.filter(category_id=category_id)
        return Event.objects.all()