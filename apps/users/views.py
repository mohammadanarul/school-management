from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from apps.helpers.mixins import DeleteModelMixin
from apps.users.models import Staff, Student
from apps.users.serializers import (
    StudentSerializer,
    StaffSerializer,
)


class StudentModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StaffModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
