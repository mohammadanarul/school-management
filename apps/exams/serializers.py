from django.utils import timezone
from rest_framework import serializers
from apps.exams.models import Exam, ExamResult
from apps.attendances.models import ExamAttendance
from apps.helpers.utils import AttendanceType


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"

    def validate(self, attrs):
        if Exam.objects.filter(
            institute=attrs["institute"],
            session=attrs["session"],
            students=attrs["students"],
            created_at__date=timezone.now().date(),
        ).exists():
            raise serializers.ValidationError("Exam Already Create")
        return attrs


class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = "__all__"

    def validate(self, attrs):
        if not ExamAttendance.objects.filter(
            exam=attrs["exam"], student=attrs["student"], subject=attrs["subject"], status=AttendanceType.PRESENT
        ):
            raise serializers.ValidationError("Sorry Student do not attend the exam")
        if ExamResult.objects.filter(
            exam=attrs["exam"],
            student=attrs["student"],
            subject=attrs["subject"],
            created_at__date=timezone.now().date(),
        ).exists():
            raise serializers.ValidationError("Alredy Exam Result create")
        return attrs
