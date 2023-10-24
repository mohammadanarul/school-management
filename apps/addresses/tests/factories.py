import factory
from faker import Faker
from apps.addresses.models import Country, Division, District, SubDistrict, Union, Ward, Address

# from apps.users.tests.factories import UserFactory

fake = Faker()


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = fake.name()


class DivisionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Division

    country = factory.SubFactory(CountryFactory)
    name = fake.name()


class DistrictFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = District

    division = factory.SubFactory(DivisionFactory)
    name = fake.name()


class SubDistrictFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SubDistrict

    district = factory.SubFactory(DistrictFactory)
    name = fake.name()


class UnionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Union

    sub_district = factory.SubFactory(SubDistrictFactory)
    name = fake.name()


class WardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ward

    union = factory.SubFactory(UnionFactory)
    name = fake.name()


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    user = factory.SubFactory("apps.users.tests.factories.UserFactory")
    country = factory.SubFactory(CountryFactory)
    division = factory.SubFactory(DivisionFactory)
    district = factory.SubFactory(DistrictFactory)
    sub_district = factory.SubFactory(SubDistrictFactory)
    union = factory.SubFactory(UnionFactory)
    ward = factory.SubFactory(WardFactory)
    moholla = fake.name()
    road_number = fake.name()
    house_number = fake.name()
