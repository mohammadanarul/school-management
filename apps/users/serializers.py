import json
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from apps.users.models import StaffProfile, Student, User, Staff, Certificate


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ("user", "certificate_type", "gpa", "session_year", "image")


class UserSerializer(serializers.ModelField):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "father_name",
            "mother_name",
            "image",
            "mobile_number",
            "email",
            "age",
            "gender",
            "blood_group",
            "date_joined",
        )


class StaffProfileSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = StaffProfile
        fields = ("id", "subjects", "salary_grade")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["created_by"] = instance.created_by.full_name if instance.created_by else ""
        representation["updated_by"] = instance.updated_by.full_name if instance.updated_by else ""
        representation["regain_date"] = instance.regain_date
        return representation


def validate_integer(value):
    if not isinstance(value, int):
        raise serializers.ValidationError("Integer field must be an integer.")
    return value


class StaffSerializer(serializers.ModelSerializer):
    staff_profile = StaffProfileSerializerOut(many=False, read_only=True)
    subjects = serializers.ListField(child=serializers.CharField(), write_only=True)
    salary_grade = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "father_name",
            "mother_name",
            "image",
            "mobile_number",
            "email",
            "age",
            "gender",
            "blood_group",
            "date_joined",
            "staff_profile",
            "subjects",
            "salary_grade",
        )

    def create(self, validated_data):
        subjects = validated_data.pop("subjects")[0].split(",")
        subjects = [int(element) for element in subjects]
        salary_grade = validated_data.pop("salary_grade")
        user = User.objects.create(**validated_data)
        profile = StaffProfile(
            user=user,
            salary_grade=salary_grade,
            created_by=self.context["request"].user,
            updated_by=self.context["request"].user,
        )
        profile.save()
        profile.subjects.set(subjects)
        return user

    def update(self, instance, validated_data):
        print('self.context["request"].user:', self.context["request"].user)
        if subjects := validated_data.get("subjects"):
            subjects = validated_data.pop("subjects")[0].split(",")
            subjects = [int(element) for element in subjects]
        if salary_grade := validated_data.get("salary_grade"):
            salary_grade = validated_data.pop("salary_grade")
        profile, create = StaffProfile.objects.get_or_create(user=instance)
        if profile:
            if salary_grade:
                profile.salary_grade = salary_grade
            profile.updated_by = self.context["request"].user
            profile.save()
            if subjects:
                profile.subjects.set(subjects)
        else:
            if salary_grade:
                create.salary_grade = salary_grade
            create.updated_by = self.context["request"].user
            create.updated_by = self.context["request"].user
            create.save()
            if subjects:
                create.subjects.set(subjects)
        instance_data = super().update(instance, validated_data)
        return instance_data


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "first_name",
            "last_name",
            "father_name",
            "mother_name",
            "image",
            "mobile_number",
            "email",
            "age",
            "gender",
            "blood_group",
        ]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_id"] = user.id
        token["name"] = f"{user.first_name} {user.last_name}"
        token["mobile_number"] = f"{user.mobile_number}"
        token["email"] = f"{user.email}"

        return token
