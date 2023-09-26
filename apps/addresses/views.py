from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from apps.helpers.mixins import DeleteModelMixin
from apps.addresses.models import (
    Country,
    Division,
    District,
    SubDistrict,
    Union,
    Word,
    Address,
)
from apps.addresses.serializers import (
    CountrySerializer,
    DivisionSerializer,
    DistrictSerializer,
    SubDistrictSerializer,
    UnionSerializer,
    WordSerializer,
    AddressSerializer,
)


class CountyModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class DivisionModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class DistrictModelViewSet(DeleteModelMixin, ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class SubDistrictModelViewSet(DeleteModelMixin, ModelViewSet):
    queryset = SubDistrict.objects.all()
    serializer_class = SubDistrictSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class UnionModelViewSet(DeleteModelMixin, ModelViewSet):
    queryset = Union.objects.all()
    serializer_class = UnionSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class WordModelViewSet(DeleteModelMixin, ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class AddressModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
