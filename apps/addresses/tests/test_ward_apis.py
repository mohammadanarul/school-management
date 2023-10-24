import pytest
from faker import Faker
from rest_framework import status

fake = Faker()

pytestmark = pytest.mark.django_db


class TestWardModelViewSet:
    base_url = "/api/v1/wards"

    def test_list_api(self, api_client, ward_factory):
        ward_factory.create_batch(15)
        response = api_client.get(f"{self.base_url}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 15
        assert len(response.data["results"]) == 10
        response = api_client.get(response.data["next"])
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 5

    def test_retrieve_api(self, api_client, ward_factory):
        district = ward_factory.create()
        response = api_client.get(f"{self.base_url}/{district.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def test_create_api(self, api_client, admin_user_token, union_factory):
        json_data = {"union": union_factory.create().id, "name": fake.name()}
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        assert response.status_code == status.HTTP_201_CREATED
        response.data["union"] == json_data["union"]
        response.data["name"] == json_data["name"]
        assert type(response.json()) == dict

    def test_update_api(self, api_client, admin_user_token, ward_factory, union_factory):
        ward = ward_factory.create()
        json_data = {"union": union_factory.create().id, "name": fake.name()}
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{ward.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        response.data["union"] == json_data["union"]
        response.data["name"] == json_data["name"]
        response.data["union"] != ward.union.id
        response.data["name"] != ward.name
        assert type(response.json()) == dict

    def test_patch_update_api(self, api_client, admin_user_token, ward_factory, union_factory):
        ward = ward_factory.create()
        json_data = {"union": union_factory.create().id}
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{ward.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        response.data["union"] == json_data["union"]
        response.data["union"] != ward.union.id
        assert type(response.json()) == dict

    def test_delete_api(self, api_client, admin_user_token, ward_factory):
        ward = ward_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{ward.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
