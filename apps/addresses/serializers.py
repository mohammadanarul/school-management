from rest_framework import serializers
from apps.addresses.models import (
    Country,
    Division,
    District,
    SubDistrict,
    Union,
    Ward,
    Address,
)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"


class SubDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDistrict
        fields = "__all__"


class UnionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Union
        fields = "__all__"


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
