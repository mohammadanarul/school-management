import pytest
from rest_framework import status
from faker import Faker

pytestmark = pytest.mark.django_db

fake = Faker()


class TestSubjectModelViewSet:
    base_url = "/api/v1/subjects"

    def test_subject_list_api(self, api_client, admin_user_token, subject_factory):
        subject_factory.create_batch(13)
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

    def test_subject_retrieve_api(self, api_client, subject_factory):
        subject = subject_factory.create()
        response = api_client.get(f"{self.base_url}/{subject.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def test_subject_create_api(self, api_client, admin_user_token, institute_factory):
        json_data = {
            "institute": institute_factory.create().id,
            "name": fake.name(),
            "code": fake.random_int(),
            "subject_type": 1,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        response_json = response.json()
        assert response.status_code == status.HTTP_201_CREATED
        assert response_json["institute"] == json_data["institute"]
        assert response_json["name"] == json_data["name"]
        assert response_json["code"] == json_data["code"]
        assert type(response_json) == dict

    def test_subject_update_api(self, api_client, admin_user_token, subject_factory, institute_factory):
        subject = subject_factory.create()
        json_data = {
            "institute": institute_factory.create().id,
            "name": fake.name(),
            "code": fake.random_int(),
            "subject_type": 1,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{subject.id}/", json_data)
        response_json = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_json["institute"] == json_data["institute"]
        assert response_json["name"] == json_data["name"]
        assert response_json["code"] == json_data["code"]
        assert type(response_json) == dict

    def test_subject_patch_update_api(self, api_client, admin_user_token, subject_factory, institute_factory):
        subject = subject_factory.create()
        json_data = {
            "name": fake.name(),
            "code": fake.random_int(),
            "subject_type": 2,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{subject.id}/", json_data)
        response_json = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_json["name"] == json_data["name"]
        assert response_json["code"] == json_data["code"]
        assert response_json["code"] != subject.code
        assert response_json["subject_type"] != subject.subject_type
        assert type(response_json) == dict

    def test_subject_delete_api(self, api_client, admin_user_token, subject_factory):
        subject = subject_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{subject.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
