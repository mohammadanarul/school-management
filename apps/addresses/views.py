from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (
    TokenAuthentication,
    BaseAuthentication,
    SessionAuthentication,
)
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
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class DivisionModelViewSet(DeleteModelMixin, ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer


class DistrictModelViewSet(DeleteModelMixin, ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class SubDistrictModelViewSet(DeleteModelMixin, ModelViewSet):
    queryset = SubDistrict.objects.all()
    serializer_class = SubDistrictSerializer


class UnionModelViewSet(DeleteModelMixin, ModelViewSet):
    queryset = Union.objects.all()
    serializer_class = UnionSerializer


class WordModelViewSet(DeleteModelMixin, ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class AddressModelViewSet(DeleteModelMixin, ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
