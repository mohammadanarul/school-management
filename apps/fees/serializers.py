from rest_framework import serializers
from apps.fees.models import Fee


class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = "__all__"
