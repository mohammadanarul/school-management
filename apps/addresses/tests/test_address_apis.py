import pytest
from faker import Faker
from rest_framework import status

fake = Faker()

pytestmark = pytest.mark.django_db


class TestAddressModelViewSet:
    base_url = "/api/v1/addresses"

    def test_list_api(self, api_client, admin_user_token, address_factory):
        address_factory.create_batch(15)
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 15
        assert len(response.data["results"]) == 10
        response = api_client.get(response.data["next"])
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 5

    def test_retrieve_api(self, api_client, admin_user_token, address_factory):
        district = address_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{district.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def test_create_api(
        self,
        api_client,
        admin_user_token,
        user_factory,
        country_factory,
        division_factory,
        district_factory,
        sub_district_factory,
        union_factory,
        ward_factory,
    ):
        json_data = {
            "user": user_factory.create().id,
            "country": country_factory.create().id,
            "division": division_factory.create().id,
            "district": district_factory.create().id,
            "sub_district": sub_district_factory.create().id,
            "union": union_factory.create().id,
            "ward": ward_factory.create().id,
            "moholla": fake.name(),
            "road_number": f"b-{fake.random_int()}",
            "house_number": f"c-{fake.random_int()}",
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        assert response.status_code == status.HTTP_201_CREATED
        response.data["user"] == json_data["user"]
        response.data["country"] == json_data["country"]
        response.data["division"] == json_data["division"]
        response.data["district"] == json_data["district"]
        response.data["sub_district"] == json_data["sub_district"]
        response.data["union"] == json_data["union"]
        response.data["ward"] == json_data["ward"]
        response.data["moholla"] == json_data["moholla"]
        response.data["road_number"] == json_data["road_number"]
        response.data["house_number"] == json_data["house_number"]
        assert type(response.json()) == dict

    def test_update_api(
        self,
        api_client,
        admin_user_token,
        address_factory,
        user_factory,
        country_factory,
        division_factory,
        district_factory,
        sub_district_factory,
        union_factory,
        ward_factory,
    ):
        address = address_factory.create()
        json_data = {
            "user": user_factory.create().id,
            "country": country_factory.create().id,
            "division": division_factory.create().id,
            "district": district_factory.create().id,
            "sub_district": sub_district_factory.create().id,
            "union": union_factory.create().id,
            "ward": ward_factory.create().id,
            "moholla": fake.name(),
            "road_number": f"b-{fake.random_int()}",
            "house_number": f"c-{fake.random_int()}",
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{address.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        response.data["user"] == json_data["user"]
        response.data["country"] == json_data["country"]
        response.data["division"] == json_data["division"]
        response.data["district"] == json_data["district"]
        response.data["sub_district"] == json_data["sub_district"]
        response.data["union"] == json_data["union"]
        response.data["moholla"] == json_data["moholla"]
        response.data["road_number"] == json_data["road_number"]
        response.data["house_number"] == json_data["house_number"]
        response.data["user"] != address.user.id
        response.data["country"] != address.country.id
        response.data["division"] != address.division.id
        response.data["district"] != address.district.id
        response.data["sub_district"] != address.sub_district.id
        response.data["union"] != address.union.id
        response.data["ward"] != address.ward.id
        response.data["moholla"] != address.moholla
        response.data["road_number"] != address.moholla
        response.data["house_number"] != address.house_number
        assert type(response.data) != dict

    def test_patch_update_api(
        self,
        api_client,
        admin_user_token,
        address_factory,
        ward_factory,
    ):
        address = address_factory.create()
        json_data = {
            "ward": ward_factory.create().id,
            "moholla": fake.name(),
            "road_number": f"b-{fake.random_int()}",
            "house_number": f"c-{fake.random_int()}",
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{address.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        response.data["ward"] == json_data["ward"]
        response.data["moholla"] == json_data["moholla"]
        response.data["road_number"] == json_data["road_number"]
        response.data["house_number"] == json_data["house_number"]
        response.data["ward"] != address.ward.id
        response.data["moholla"] != address.moholla
        response.data["road_number"] != address.moholla
        response.data["house_number"] != address.house_number
        assert type(response.data) != dict

    def test_delete_api(self, api_client, admin_user_token, address_factory):
        address = address_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{address.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
