import pytest
from faker import Faker
from rest_framework import status

fake = Faker()

pytestmark = pytest.mark.django_db


class TestDivisionModelViewSet:
    base_url = "/api/v1/divisions"

    def test_list_api(self, api_client, division_factory):
        division_factory.create_batch(15)
        response = api_client.get(f"{self.base_url}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 15
        assert len(response.data["results"]) == 10
        response = api_client.get(response.data["next"])
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 5

    def test_retrieve_api(self, api_client, division_factory):
        division = division_factory.create()
        response = api_client.get(f"{self.base_url}/{division.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def test_create_api(self, api_client, admin_user_token, country_factory):
        json_data = {"country": country_factory.create().id, "name": fake.name()}
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        assert response.status_code == status.HTTP_201_CREATED
        response.data["country"] == json_data["country"]
        response.data["name"] == json_data["name"]
        assert type(response.json()) == dict

    def test_update_api(self, api_client, admin_user_token, division_factory, country_factory):
        division = division_factory.create()
        country = country_factory.create()
        json_data = {"country": country_factory.create().id, "name": fake.name()}
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{division.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        response.data["country"] == json_data["country"]
        response.data["name"] == json_data["name"]
        response.data["country"] != country.id
        response.data["name"] != country.name
        assert type(response.json()) == dict

    def test_patch_update_api(self, api_client, admin_user_token, division_factory, country_factory):
        division = division_factory.create()
        country = country_factory.create()
        json_data = {"country": country_factory.create().id}
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{division.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        response.data["country"] == json_data["country"]
        response.data["country"] != country.id
        assert type(response.json()) == dict

    def test_delete_api(self, api_client, admin_user_token, division_factory):
        division = division_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{division.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
