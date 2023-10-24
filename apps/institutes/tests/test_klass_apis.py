import pytest
from rest_framework import status
from faker import Faker

pytestmark = pytest.mark.django_db

fake = Faker()


class TestKlassModelViewSet:
    base_url = "/api/v1/klass"

    def test_klass_list_api(self, api_client, admin_user_token, klass_factory):
        klass_factory.create_batch(13)
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 13
        assert len(response.data["results"]) == 10
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(response.data["next"])
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3

    def test_klass_retrieve_api(self, api_client, admin_user_token, klass_factory):
        klass = klass_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{klass.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def test_klass_create_api(self, api_client, admin_user_token, institute_factory, subject_factory):
        subjects = subject_factory.create_batch(2)
        json_data = {
            "institute": institute_factory.create().id,
            "name": fake.name(),
            "seats": 50,
            "subjects": [subjects[0].id, subjects[1].id],
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        response_json = response.json()
        assert response.status_code == status.HTTP_201_CREATED
        assert response_json["institute"] == json_data["institute"]
        assert response_json["name"] == json_data["name"]
        assert response_json["seats"] == json_data["seats"]
        assert response_json["subjects"] == json_data["subjects"]
        assert type(response_json) == dict

    def test_klass_update_api(self, api_client, admin_user_token, klass_factory, institute_factory, subject_factory):
        klass = klass_factory.create()
        subjects = subject_factory.create_batch(2)
        json_data = {
            "institute": institute_factory.create().id,
            "name": fake.name(),
            "seats": 50,
            "subjects": [subjects[0].id, subjects[1].id],
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{klass.id}/", json_data)
        response_json = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_json["institute"] == json_data["institute"]
        assert response_json["name"] == json_data["name"]
        assert response_json["seats"] == json_data["seats"]
        assert response_json["subjects"] == json_data["subjects"]
        assert type(response_json) == dict

    def test_klass_patch_update_api(self, api_client, admin_user_token, klass_factory, subject_factory):
        klass = klass_factory.create()
        subjects = subject_factory.create_batch(2)
        json_data = {
            "seats": 52,
            "subjects": [subjects[0].id, subjects[1].id],
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{klass.id}/", json_data)
        response_json = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_json["seats"] == json_data["seats"]
        assert response_json["subjects"] == json_data["subjects"]
        assert response_json["seats"] != klass.seats
        assert response_json["subjects"] != klass.subjects
        assert type(response_json) == dict

    def test_klass_delete_api(self, api_client, admin_user_token, klass_factory):
        klass = klass_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{klass.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
