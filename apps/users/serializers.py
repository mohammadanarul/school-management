from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from apps.users.models import User, Student, Staff, Certificate


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ("user", "certificate_type", "gpa", "session_year", "image")


class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "unique_id",
            "first_name",
            "last_name",
            "mobile_number",
            "email",
            "age",
            "gender",
            "blood_group",
        )


class StaffUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "unique_id",
            "first_name",
            "last_name",
            "mobile_number",
            "email",
            "age",
            "gender",
            "blood_group",
        )


class StudentSerializer(WritableNestedModelSerializer):
    user = StudentUserSerializer()
    certificates = CertificateSerializer(many=True)

    class Meta:
        model = Student
        fields = ("id", "user", "father_name", "mother_name", "image", "certificates")


class StaffSerializer(WritableNestedModelSerializer):
    certificates = CertificateSerializer(many=True)
    user = StaffUserSerializer(many=False)

    class Meta:
        model = Staff
        fields = ("id", "user", "father_name", "mother_name", "image", "certificates")


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["user_id"] = user.id
        token["name"] = f"{user.first_name} {user.last_name}"
        token["mobile_number"] = f"{user.mobile_number}"
        token["email"] = f"{user.email}"

        return token
