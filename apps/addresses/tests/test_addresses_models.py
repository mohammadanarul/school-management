import pytest


pytestmark = pytest.mark.django_db


class TestCountryModel:
    def test_return_str(self, country_factory):
        country = country_factory.create()
        assert country.__str__() == country.name


class TestDivisionModel:
    def test_return_str(self, division_factory):
        division = division_factory.create()
        assert division.__str__() == division.name


class TestDistrictModel:
    def test_return_str(self, district_factory):
        district = district_factory.create()
        assert district.__str__() == district.name


class TestSubDistrictModel:
    def test_return_str(self, sub_district_factory):
        sub_district = sub_district_factory.create()
        assert sub_district.__str__() == sub_district.name


class TestUnionModel:
    def test_return_str(self, union_factory):
        union = union_factory.create()
        assert union.__str__() == union.name


class TestWardModel:
    def test_return_str(self, ward_factory):
        ward = ward_factory.create()
        assert ward.__str__() == ward.name


class TestAddressModel:
    def test_return_str(self, address_factory):
        address = address_factory.create()
        assert address.__str__() == address.user.first_name
