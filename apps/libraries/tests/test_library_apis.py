import pytest
from faker import Faker
from rest_framework import status

fake = Faker()

pytestmark = pytest.mark.django_db


class TestLibraryModelViewSet:
    base_url = "/api/v1/libraries"

    def test_list_api(self, api_client, library_factory):
        library_factory.create_batch(15)
        response = api_client.get(f"{self.base_url}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 15
        assert len(response.data["results"]) == 10
        response = api_client.get(response.data["next"])
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 5
        assert type(response.data) == dict

    def test_retrieve_api(self, api_client, admin_user_token, library_factory):
        library = library_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{library.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def test_create_api(self, api_client, admin_user_token, institute_factory):
        json_data = {"institute": institute_factory.create().id, "name": fake.name(), "established_date": fake.date()}
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        assert response.status_code == status.HTTP_201_CREATED
        response.data["institute"] == json_data["institute"]
        response.data["name"] == json_data["name"]
        response.data["established_date"] == json_data["established_date"]
        assert type(response.json()) == dict

    def test_update_api(self, api_client, admin_user_token, library_factory, institute_factory):
        library = library_factory.create()
        json_data = {"institute": institute_factory.create().id, "name": fake.name(), "established_date": fake.date()}
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{library.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        response.data["institute"] == json_data["institute"]
        response.data["name"] == json_data["name"]
        response.data["established_date"] == json_data["established_date"]
        response.data["institute"] != library.institute.id
        response.data["name"] != library.name
        response.data["established_date"] != library.established_date
        assert type(response.json()) == dict

    def test_patch_update_api(self, api_client, admin_user_token, library_factory, institute_factory):
        library = library_factory.create()
        json_data = {"institute": institute_factory.create().id, "name": fake.name()}
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{library.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        response.data["institute"] == json_data["institute"]
        response.data["name"] == json_data["name"]
        response.data["institute"] != library.institute.id
        response.data["name"] != library.name
        assert type(response.json()) == dict

    def test_delete_api(self, api_client, admin_user_token, library_factory):
        library = library_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{library.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
