from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import (
    JWTAuthentication,
)
from rest_framework.permissions import IsAdminUser, AllowAny
from apps.events.models import Event
from apps.events.serializers import EventSerializer


class EventModelViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.action == "list":
            return [AllowAny()]
        else:
            return [IsAdminUser()]
