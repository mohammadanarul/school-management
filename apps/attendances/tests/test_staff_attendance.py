import pytest
from rest_framework import status
from faker import Faker

pytestmark = pytest.mark.django_db

fake = Faker()


class TestStaffAttendaceModelViewSet:
    base_url = "/api/v1/staff-attedances"

    def test_list_api(self, api_client, admin_user_token, staff_attendance_factory):
        staff_attendance_factory.create_batch(13)
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

    def test_retrieve_api(self, api_client, admin_user_token, staff_attendance_factory):
        attendance = staff_attendance_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{attendance.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def test_create_api(self, api_client, admin_user_token, institute_factory, user_factory):
        json_data = {
            "institute": institute_factory.create().id,
            "staff_user": user_factory.create().id,
            "status": 1,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["institute"] == json_data["institute"]
        assert response.data["staff_user"] == json_data["staff_user"]
        assert response.data["status"] == json_data["status"]
        assert type(response.json()) == dict

    def test_update_api(
        self,
        api_client,
        admin_user_token,
        staff_attendance_factory,
        institute_factory,
        user_factory,
    ):
        attendance = staff_attendance_factory.create()
        json_data = {
            "institute": institute_factory.create().id,
            "staff_user": user_factory.create().id,
            "status": 2,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{attendance.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["institute"] == json_data["institute"]
        assert response.data["staff_user"] == json_data["staff_user"]
        assert response.data["status"] == json_data["status"]
        assert response.data["institute"] != attendance.institute.id
        assert response.data["staff_user"] != attendance.staff_user.id
        assert response.data["status"] != attendance.status.value
        assert type(response.json()) == dict

    def test_patch_update_api(self, api_client, admin_user_token, staff_attendance_factory):
        attendance = staff_attendance_factory.create()
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

    def test_delete_api(self, api_client, admin_user_token, staff_attendance_factory):
        attendance = staff_attendance_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{attendance.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
