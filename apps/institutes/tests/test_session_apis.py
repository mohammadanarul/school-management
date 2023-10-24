import pytest
from rest_framework import status
from faker import Faker

pytestmark = pytest.mark.django_db

fake = Faker()


class TestSessionModelViewSet:
    base_url = "/api/v1/sessions"

    def test_session_list_api(self, api_client, admin_user_token, session_factory):
        session_factory.create_batch(13)
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

    def test_session_retrieve_api(self, api_client, admin_user_token, session_factory):
        session = session_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{session.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def test_session_create_api(self, api_client, admin_user_token, institute_factory, klass_factory, student_factory):
        students = student_factory.create_batch(2)
        json_data = {
            "institute": institute_factory.create().id,
            "klass": klass_factory.create().id,
            "year": 50,
            "students": [students[0].id, students[1].id],
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        response_json = response.json()
        assert response.status_code == status.HTTP_201_CREATED
        assert response_json["institute"] == json_data["institute"]
        assert response_json["students"] == json_data["students"]
        assert type(response_json) == dict

    def test_session_update_api(
        self, api_client, admin_user_token, session_factory, institute_factory, klass_factory, student_factory
    ):
        session = session_factory.create()
        students = student_factory.create_batch(2)
        json_data = {
            "institute": institute_factory.create().id,
            "klass": klass_factory.create().id,
            "year": 50,
            "students": [students[0].id, students[1].id],
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{session.id}/", json_data)
        response_json = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_json["institute"] == json_data["institute"]
        assert response_json["students"] == json_data["students"]
        assert type(response_json) == dict

    def test_session_patch_update_api(self, api_client, admin_user_token, session_factory, student_factory):
        session = session_factory.create()
        students = student_factory.create_batch(2)
        json_data = {
            "year": fake.year(),
            "students": [students[0].id, students[1].id],
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{session.id}/", json_data)
        response_json = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_json["students"] == json_data["students"]
        assert response_json["year"] != session.year
        assert response_json["students"] != session.students
        assert type(response_json) == dict

    def test_session_delete_api(self, api_client, admin_user_token, session_factory):
        session = session_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{session.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
