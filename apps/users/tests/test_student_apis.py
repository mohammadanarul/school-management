import pytest
import io
from faker import Faker
from PIL import Image
from rest_framework import status
from apps.helpers.helpers import bd_number_generator

pytestmark = pytest.mark.django_db

fake = Faker()


class TestStudentModelViewSet:
    base_url = "/api/v1/students"

    def test_get_student_list_api(self, api_client, admin_user_token, student_factory):
        student_factory.create_batch(12)
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 12
        assert len(response.data["results"]) == 10
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(response.data["next"])
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 2
        assert type(response.json()) == dict

    def test_student_retrieve_api(self, api_client, admin_user_token, student_factory):
        student = student_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{student.id}/")
        assert response.status_code == status.HTTP_200_OK
        print("response_data: ", response.json())
        assert type(response.json()) == dict

    def generate_photo(self):
        file = io.BytesIO()
        image = Image.new("RGBA", size=(100, 100), color=(155, 0, 0))
        image.save(file, "png")
        file.name = "test.png"
        file.seek(0)
        return file

    def test_student_create_api(self, api_client, admin_user_token):
        form_data = {
            "first_name": fake.name(),
            "last_name": "islam",
            "father_name": fake.name(),
            "mother_name": fake.name(),
            "mobile_number": bd_number_generator(),
            "image": self.generate_photo(),
            "email": fake.email(),
            "age": 25,
            "gender": 1,
            "blood_group": 1,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", form_data, format="multipart")
        assert response.status_code == status.HTTP_201_CREATED
        assert type(response.json()) == dict

    def test_student_update_api(self, api_client, admin_user_token, student_factory):
        student = student_factory.create()
        form_data = {
            "id": student.id,
            "first_name": fake.name(),
            "last_name": "islam",
            "father_name": fake.name(),
            "mother_name": fake.name(),
            "mobile_number": bd_number_generator(),
            "image": self.generate_photo(),
            "email": fake.email(),
            "age": 25,
            "gender": 1,
            "blood_group": 1,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{student.id}/", form_data, format="multipart")
        assert response.status_code == status.HTTP_200_OK
        response_json = response.json()
        assert response_json["first_name"] == form_data["first_name"]
        assert response_json["mobile_number"] == form_data["mobile_number"]
        assert response_json["email"] == form_data["email"]
        assert type(response_json) == dict

    def test_student_patch_update_api(self, api_client, admin_user_token, student_factory):
        student = student_factory.create()
        form_data = {
            "last_name": "islam (update)",
            "father_name": fake.name(),
            "mother_name": fake.name(),
            "mobile_number": bd_number_generator(),
            "image": self.generate_photo(),
            "email": fake.email(),
            "age": 27,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{student.id}/", form_data, format="multipart")
        assert response.status_code == status.HTTP_200_OK
        response_json = response.json()
        assert response_json["father_name"] == form_data["father_name"]
        assert response_json["mobile_number"] == form_data["mobile_number"]
        assert response_json["email"] == form_data["email"]
        assert type(response_json) == dict

    def test_student_delete_api(self, api_client, admin_user_token, student_factory):
        student = student_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{student.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
