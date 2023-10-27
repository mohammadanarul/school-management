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

    def create(self, validated_data):
        if not ExamAttendance.objects.filter(
            exam=validated_data.get("exam"),
            student=validated_data.get("student"),
            subject=validated_data.get("subject"),
            status=AttendanceType.PRESENT,
        ).exists():
            raise serializers.ValidationError("Sorry, Student do not attend in the exam")
        if ExamResult.objects.filter(
            exam=validated_data.get("exam"),
            student=validated_data.get("student"),
            subject=validated_data.get("subject"),
            created_at__date=timezone.now().date(),
        ).exists():
            raise serializers.ValidationError("Alredy Exam Result create")
        obj = ExamResult.objects.create(**validated_data)
        return obj

    def update(self, instance, validated_data):
        if not ExamAttendance.objects.filter(
            exam=validated_data.get("exam") if validated_data.get("exam") else instance.exam.id,
            student=validated_data.get("student") if validated_data.get("student") else instance.student.id,
            subject=validated_data.get("subject") if validated_data.get("subject") else instance.subject.id,
            status=AttendanceType.PRESENT,
        ).exists():
            raise serializers.ValidationError("Sorry, Student do not attend in the exam")
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
