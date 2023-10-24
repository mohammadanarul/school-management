import pytest
from faker import Faker
from rest_framework import status
from apps.helpers.utils import DayChoices

fake = Faker()

pytestmark = pytest.mark.django_db


class TestRoutineModelViewSet:
    base_url = "/api/v1/routines"

    def test_list_api(self, api_client, routine_factory):
        routine_factory.create_batch(15)
        response = api_client.get(f"{self.base_url}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 15
        assert len(response.data["results"]) == 10
        response = api_client.get(response.data["next"])
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 5

    def test_retrieve_api(self, api_client, admin_user_token, routine_factory):
        routine_obj = routine_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{routine_obj.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def test_create_api(self, api_client, admin_user_token, klass_factory, teacher_factory, subject_factory):
        json_data = {
            "klass": klass_factory.create().id,
            "teacher": teacher_factory.create().id,
            "subject": subject_factory.create().id,
            "day": DayChoices.MONDAY,
            "time": fake.time(),
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", json_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["klass"] == json_data["klass"]
        assert response.data["teacher"] == json_data["teacher"]
        assert response.data["subject"] == json_data["subject"]
        assert response.data["day"] == json_data["day"]
        assert response.data["time"] == json_data["time"]
        assert type(response.json()) == dict

    def test_update_api(
        self, api_client, admin_user_token, routine_factory, klass_factory, teacher_factory, subject_factory
    ):
        routine_obj = routine_factory.create()
        json_data = {
            "klass": klass_factory.create().id,
            "teacher": teacher_factory.create().id,
            "subject": subject_factory.create().id,
            "day": DayChoices.MONDAY,
            "time": fake.time(),
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{routine_obj.id}/", json_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["klass"] == json_data["klass"]
        assert response.data["teacher"] == json_data["teacher"]
        assert response.data["subject"] == json_data["subject"]
        assert response.data["day"] == json_data["day"]
        assert response.data["time"] == json_data["time"]
        assert response.data["klass"] != routine_obj.klass.id
        assert response.data["teacher"] != routine_obj.teacher.id
        assert response.data["subject"] != routine_obj.subject.id
        assert response.data["day"] != routine_obj.day
        assert response.data["time"] != routine_obj.time
        assert type(response.json()) == dict

    def test_patch_update_api(self, api_client, admin_user_token, routine_factory, teacher_factory, subject_factory):
        routine_obj = routine_factory.create()
        json_data = {
            "teacher": teacher_factory.create().id,
            "subject": subject_factory.create().id,
            "day": DayChoices.WEDNESDAY,
            "time": fake.time(),
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{routine_obj.id}/", json_data)
        assert response.status_code == 200
        assert response.status_code == status.HTTP_200_OK
        assert response.data["teacher"] == json_data["teacher"]
        assert response.data["subject"] == json_data["subject"]
        assert response.data["day"] == json_data["day"]
        assert response.data["time"] == json_data["time"]
        assert response.data["teacher"] != routine_obj.teacher.id
        assert response.data["subject"] != routine_obj.subject.id
        assert response.data["day"] != routine_obj.day
        assert response.data["time"] != routine_obj.time
        assert type(response.json()) == dict

    def test_delete_api(self, api_client, admin_user_token, routine_factory):
        routine_obj = routine_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{routine_obj.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
