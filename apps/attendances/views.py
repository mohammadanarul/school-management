from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from apps.attendances.models import Attendance, StaffAttendance, ExamAttendance
from apps.attendances.serializers import (
    AttendanceSerializer,
    ExamAttendaceSerializer,
    StaffAttendanceSerializer,
)


class AttendanceModelViewSet(ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class StaffAttendanceModelViewSet(ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAdminUser]
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer


class ExamAttendanceModelViewSet(ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAdminUser]
    queryset = ExamAttendance.objects.all()
    serializer_class = ExamAttendaceSerializer
