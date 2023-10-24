import pytest
from rest_framework import status
from faker import Faker

pytestmark = pytest.mark.django_db

fake = Faker()


class TestExamAttendanceModelViewSet:
    base_url = "/api/v1/exam-attendances"

    def test_list_api(self, api_client, admin_user_token, exam_attendance_factory):
        exam_attendance_factory.create_batch(13)
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

    def test_retrieve_api(self, api_client, admin_user_token, exam_attendance_factory):
        attendance = exam_attendance_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{attendance.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def test_create_api(
        self,
        api_client,
        admin_user_token,
        institute_factory,
        klass_factory,
        exam_factory,
        student_factory,
        subject_factory,
    ):
        json_data = {
            "institute": institute_factory.create().id,
            "klass": klass_factory.create().id,
            "exam": exam_factory.create().id,
            "student": student_factory.create().id,
            "subject": subject_factory.create().id,
            "status": 1,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["institute"] == json_data["institute"]
        assert response.data["exam"] == json_data["exam"]
        assert response.data["klass"] == json_data["klass"]
        assert response.data["student"] == json_data["student"]
        assert response.data["subject"] == json_data["subject"]
        assert response.data["status"] == json_data["status"]
        assert type(response.json()) == dict

    def test_update_api(
        self,
        api_client,
        admin_user_token,
        exam_attendance_factory,
        institute_factory,
        klass_factory,
        exam_factory,
        student_factory,
        subject_factory,
    ):
        attendance = exam_attendance_factory.create()
        json_data = {
            "institute": institute_factory.create().id,
            "klass": klass_factory.create().id,
            "exam": exam_factory.create().id,
            "student": student_factory.create().id,
            "subject": subject_factory.create().id,
            "status": 2,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{attendance.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["institute"] == json_data["institute"]
        assert response.data["klass"] == json_data["klass"]
        assert response.data["exam"] == json_data["exam"]
        assert response.data["student"] == json_data["student"]
        assert response.data["subject"] == json_data["subject"]
        assert response.data["status"] == json_data["status"]
        assert response.data["institute"] != attendance.institute
        assert response.data["klass"] != attendance.klass
        assert response.data["exam"] != attendance.exam
        assert response.data["student"] != attendance.student
        assert response.data["subject"] != attendance.subject
        assert response.data["status"] != attendance.status
        assert type(response.json()) == dict

    def test_patch_update_api(self, api_client, admin_user_token, exam_attendance_factory):
        attendance = exam_attendance_factory.create()
        json_data = {
            "status": 2,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{attendance.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["status"] == json_data["status"]
        assert response.data["status"] != attendance.status
        assert type(response.json()) == dict

    def test_delete_api(self, api_client, admin_user_token, exam_attendance_factory):
        attendance = exam_attendance_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{attendance.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
