from rest_framework import serializers
from apps.attendances.models import StaffAttendance, Attendance, ExamAttendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        exclude = ("students",)


class StaffAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        mdoel = StaffAttendance
        exclude = ("staff",)


class ExamAttendaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamAttendance
        fields = "__all__"
