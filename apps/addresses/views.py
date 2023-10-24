from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.helpers.mixins import DeleteModelMixin
from apps.addresses.models import (
    Country,
    Division,
    District,
    SubDistrict,
    Union,
    Ward,
    Address,
)
from apps.addresses.serializers import (
    CountrySerializer,
    DivisionSerializer,
    DistrictSerializer,
    SubDistrictSerializer,
    UnionSerializer,
    WardSerializer,
    AddressSerializer,
)


class CountyModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class DivisionModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class DistrictModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class SubDistrictModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = SubDistrict.objects.all()
    serializer_class = SubDistrictSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class UnionModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Union.objects.all()
    serializer_class = UnionSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class WardModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Ward.objects.all()
    serializer_class = WardSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class AddressModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
