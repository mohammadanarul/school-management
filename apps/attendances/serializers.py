from rest_framework import serializers
from apps.attendances.models import StaffAttendance, Attendance, ExamAttendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class StaffAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAttendance
        fields = "__all__"


class ExamAttendaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamAttendance
        fields = "__all__"
