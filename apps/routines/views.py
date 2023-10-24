from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny
from apps.helpers.mixins import ModelViewSetMixin
from apps.routines.models import Routine
from apps.routines.serializers import RoutineSerializer


class RoutineModelViewSet(ModelViewSetMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Routine.objects.select_related("klass").all()
    serializer_class = RoutineSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrive":
            return [AllowAny()]
        else:
            return [IsAdminUser()]
