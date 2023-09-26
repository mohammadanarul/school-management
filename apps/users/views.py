from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser
from apps.users.models import User
from apps.users.serializers import (
    StudentSerializer,
    StaffSerializer,
)


class StudentModelViewSet(ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = StudentSerializer


class StaffModelViewSet(ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = StaffSerializer

    def get_permissions(self):
        if self.action == "list":
            return [AllowAny()]
        else:
            return [IsAdminUser()]
