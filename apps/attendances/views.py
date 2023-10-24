from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from apps.helpers.mixins import ModelViewSetMixin
from apps.attendances.models import Attendance, StaffAttendance, ExamAttendance
from apps.attendances.serializers import (
    AttendanceSerializer,
    ExamAttendaceSerializer,
    StaffAttendanceSerializer,
)


class AttendanceModelViewSet(ModelViewSetMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class StaffAttendanceModelViewSet(ModelViewSetMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer


class ExamAttendanceModelViewSet(ModelViewSetMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = ExamAttendance.objects.all()
    serializer_class = ExamAttendaceSerializer
