import pytest
from faker import Faker
from rest_framework import status

fake = Faker()

pytestmark = pytest.mark.django_db


class TestDistrictModelViewSet:
    base_url = "/api/v1/districts"

    def test_list_api(self, api_client, district_factory):
        district_factory.create_batch(15)
        response = api_client.get(f"{self.base_url}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 15
        assert len(response.data["results"]) == 10
        response = api_client.get(response.data["next"])
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 5

    def test_retrieve_api(self, api_client, district_factory):
        district = district_factory.create()
        response = api_client.get(f"{self.base_url}/{district.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def test_create_api(self, api_client, admin_user_token, division_factory):
        json_data = {"division": division_factory.create().id, "name": fake.name()}
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        assert response.status_code == status.HTTP_201_CREATED
        response.data["division"] == json_data["division"]
        response.data["name"] == json_data["name"]
        assert type(response.json()) == dict

    def test_update_api(self, api_client, admin_user_token, district_factory, division_factory):
        district = district_factory.create()
        division = division_factory.create()
        json_data = {"division": division_factory.create().id, "name": fake.name()}
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{district.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        response.data["division"] == json_data["division"]
        response.data["name"] == json_data["name"]
        response.data["division"] != division.id
        response.data["name"] != division.name
        assert type(response.json()) == dict

    def test_patch_update_api(self, api_client, admin_user_token, district_factory, division_factory):
        district = district_factory.create()
        division = division_factory.create()
        json_data = {"division": division_factory.create().id}
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{district.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        response.data["division"] == json_data["division"]
        response.data["division"] != division.id
        assert type(response.json()) == dict

    def test_delete_api(self, api_client, admin_user_token, district_factory):
        district = district_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{district.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
