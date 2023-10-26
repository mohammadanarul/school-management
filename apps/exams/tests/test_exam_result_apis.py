import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestExamResultModelViewSet:
    base_url = "/api/v1/exam_results"

    def test_unathorized_api(self, api_client, exam_result_factory):
        exam_restult = exam_result_factory.create()
        response = api_client.get(f"{self.base_url}/{exam_restult.id}/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_permission_api(self, api_client, user_token, exam_result_factory):
        exam_restult = exam_result_factory.create()
        jwt_token = user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{exam_restult.id}/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_not_found_api(self, api_client, admin_user_token, exam_result_factory):
        exam_result_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/3/")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_bad_request_api(self, api_client, admin_user_token, exam_attendance_factory):
        """⚠️ required field or body missing and 400 bad request error showing"""
        exam_attendance = exam_attendance_factory.create()
        json_data = {
            "student": exam_attendance.student.id,
            "subject": exam_attendance.subject.id,
            "gpa": 3.12,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_parmanent_redirect_append_slash_api(self, api_client, admin_user_token):
        """⚠️ wrong_url: f"{self.base_url}", right_url: f"{self.base_url}/" missing slash"""
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}")
        assert response.status_code == status.HTTP_301_MOVED_PERMANENTLY

    def test_list_api(self, api_client, admin_user_token, exam_result_factory):
        exam_result_factory.create_batch(15)
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 15
        assert len(response.data["results"]) == 10
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(response.data["next"])
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 5

    def test_retrieve_api(self, api_client, admin_user_token, exam_result_factory):
        exam_restult = exam_result_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{exam_restult.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def test_create_api(self, api_client, admin_user_token, exam_attendance_factory):
        exam_attendance = exam_attendance_factory.create()
        json_data = {
            "exam": exam_attendance.exam.id,
            "student": exam_attendance.student.id,
            "subject": exam_attendance.subject.id,
            "gpa": 3.12,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["exam"] == json_data["exam"]
        assert response.data["student"] == json_data["student"]
        assert response.data["subject"] == json_data["subject"]
        assert response.data["gpa"] == json_data["gpa"]
        assert type(response.json()) == dict

    def test_update_api(
        self,
        api_client,
        admin_user_token,
        exam_result_factory,
        exam_attendance_factory,
    ):
        exam_attendance = exam_attendance_factory.create()
        exam_result = exam_result_factory.create()
        json_data = {
            "exam": exam_attendance.exam.id,
            "student": exam_attendance.student.id,
            "subject": exam_attendance.subject.id,
            "gpa": 3.32,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{exam_result.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["exam"] == json_data["exam"]
        assert response.data["student"] == json_data["student"]
        assert response.data["subject"] == json_data["subject"]
        assert response.data["gpa"] == json_data["gpa"]
        assert response.data["exam"] != exam_result.exam
        assert response.data["student"] != exam_result.student
        assert response.data["subject"] != exam_result.subject
        assert response.data["gpa"] != exam_result.gpa
        assert type(response.json()) == dict

    def test_patch_update_api(self, api_client, admin_user_token, exam_result_factory, exam_attendance_factory):
        exam_attendance = exam_attendance_factory.create()
        exam_result = exam_result_factory.create(
            exam=exam_attendance.exam, student=exam_attendance.student, subject=exam_attendance.subject
        )
        json_data = {
            "gpa": 3.32,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{exam_result.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["gpa"] == json_data["gpa"]
        assert response.data["gpa"] != exam_result.gpa
        assert type(response.json()) == dict

    def test_delete_api(self, api_client, admin_user_token, exam_result_factory):
        exam_result = exam_result_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{exam_result.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
