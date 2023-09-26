from rest_framework import serializers
from apps.institutes.models import Institute, Subject, Klass, Session


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = "__all__"


class SubjectSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class KlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"
