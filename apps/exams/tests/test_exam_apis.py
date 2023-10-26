import pytest
from rest_framework import status
from faker import Faker

pytestmark = pytest.mark.django_db

fake = Faker()


class TestExamModelViewSet:
    base_url = "/api/v1/exams"

    def test_list_api(self, api_client, admin_user_token, exam_factory):
        exam_factory.create_batch(13)
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

    def test_retrieve_api(self, api_client, admin_user_token, exam_factory):
        exam = exam_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{exam.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def test_create_api(self, api_client, admin_user_token, institute_factory, session_factory, student_factory):
        students = student_factory.create_batch(2)
        json_data = {
            "institute": institute_factory.create().id,
            "session": session_factory.create().id,
            "exam_type": 1,
            "status": 1,
            "students": [students[0].id, students[1].id],
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        response_json = response.json()
        assert response.status_code == status.HTTP_201_CREATED
        assert response_json["institute"] == json_data["institute"]
        assert response_json["session"] == json_data["session"]
        assert response_json["exam_type"] == json_data["exam_type"]
        assert response_json["status"] == json_data["status"]
        assert response_json["students"] == json_data["students"]
        assert type(response_json) == dict

    def test_update_api(
        self, api_client, admin_user_token, exam_factory, institute_factory, session_factory, student_factory
    ):
        exam = exam_factory.create()
        students = student_factory.create_batch(2)
        json_data = {
            "institute": institute_factory.create().id,
            "session": session_factory.create().id,
            "exam_type": 2,
            "status": 2,
            "students": [students[0].id, students[1].id],
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{exam.id}/", json_data)
        print("exam_respons: ", response.data)
        response_json = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_json["institute"] == json_data["institute"]
        assert response_json["session"] == json_data["session"]
        assert response_json["exam_type"] == json_data["exam_type"]
        assert response_json["status"] == json_data["status"]
        assert response_json["students"] == json_data["students"]
        assert response_json["students"] != exam.students
        assert response_json["institute"] != exam.institute
        assert response_json["session"] != exam.session
        assert response_json["exam_type"] != exam.exam_type
        assert response_json["status"] != exam.status
        assert type(response_json) == dict

    def test_patch_update_api(self, api_client, admin_user_token, exam_factory, student_factory):
        exam = exam_factory.create()
        students = student_factory.create_batch(2)
        json_data = {
            "exam_type": 2,
            "status": 2,
            "students": [students[0].id, students[1].id],
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{exam.id}/", json_data)
        response_json = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_json["exam_type"] == json_data["exam_type"]
        assert response_json["status"] == json_data["status"]
        assert response_json["students"] != exam.students
        assert response_json["exam_type"] != exam.exam_type
        assert response_json["status"] != exam.status
        assert type(response_json) == dict

    def test_delete_api(self, api_client, admin_user_token, exam_factory):
        exam = exam_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{exam.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
