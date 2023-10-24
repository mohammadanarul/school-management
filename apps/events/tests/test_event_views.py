import pytest
import io
from PIL import Image
from faker import Faker
from rest_framework import status

fake = Faker()

pytestmark = pytest.mark.django_db


class TestEventModelViewSet:
    base_url = "/api/v1/events"

    def test_event_list_api(self, api_client, event_factory):
        event_factory.create_batch(15)
        response = api_client.get(f"{self.base_url}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 15
        assert len(response.data["results"]) == 10
        response = api_client.get(response.data["next"])
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 5

    def test_event_retrieve_api(self, api_client, admin_user_token, event_factory):
        event_obj = event_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{event_obj.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def generate_photo(self):
        file = io.BytesIO()
        image = Image.new("RGBA", size=(100, 100), color=(155, 0, 0))
        image.save(file, "png")
        file.name = "test.png"
        file.seek(0)
        return file

    def test_event_create_api(self, api_client, admin_user_token):
        data = {
            "session_year": fake.year(),
            "name": fake.name(),
            "banner": self.generate_photo(),
            "group_image": self.generate_photo(),
            "date": fake.date(),
            "cost_balance": fake.random_int(),
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", data, format="multipart")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["session_year"] == int(data["session_year"])
        assert response.data["name"] == data["name"]
        assert response.data["date"] == data["date"]
        assert type(response.json()) == dict

    def test_event_update_api(self, api_client, admin_user_token, event_factory):
        evnt_obj = event_factory.create()
        data = {
            "session_year": int(fake.year()),
            "name": fake.name(),
            "date": fake.date(),
            "banner": self.generate_photo(),
            "group_image": self.generate_photo(),
            "cost_balance": fake.random_int(),
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{evnt_obj.id}/", data, format="multipart")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["session_year"] == data["session_year"]
        assert response.data["name"] == data["name"]
        assert response.data["cost_balance"] == data["cost_balance"]
        assert response.data["session_year"] != evnt_obj.session_year
        assert response.data["name"] != evnt_obj.name
        assert response.data["cost_balance"] != evnt_obj.cost_balance
        assert type(response.json()) == dict

    def test_event_patch_update_api(self, api_client, admin_user_token, event_factory):
        event_obj = event_factory.create()
        data = {
            "name": fake.name(),
            "session_year": int(fake.year()),
            "cost_balance": 10.3,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{event_obj.id}/", data)
        assert response.status_code == 200
        returned_json = response.json()
        assert returned_json["name"] == data["name"]
        assert returned_json["session_year"] == data["session_year"]
        assert returned_json["cost_balance"] == data["cost_balance"]
        assert returned_json["name"] != event_obj.name
        assert returned_json["session_year"] != int(event_obj.session_year)
        assert returned_json["cost_balance"] != event_obj.cost_balance
        assert type(returned_json) == dict

    def test_event_delete_api(self, api_client, admin_user_token, event_factory):
        event_obj = event_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{event_obj.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
