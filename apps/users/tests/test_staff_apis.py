import pytest
import io
from PIL import Image
from rest_framework import status
from faker import Faker
from apps.helpers.helpers import bd_number_generator

pytestmark = pytest.mark.django_db

fake = Faker()


class TestStaffModelViewSet:
    base_url = "/api/v1/staffs"

    def test_get_staff_list_api(self, api_client, admin_user_token, staff_factory):
        staff_factory.create_batch(12)
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

    def test_staff_retrieve_api(self, api_client, admin_user_token, staff_factory):
        staff_user = staff_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{staff_user.id}/")
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

    def test_staff_create_api(self, api_client, admin_user_token, subject_factory):
        subject = subject_factory.create_batch(2)
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
            "date_joined": fake.date(),
            "subjects": f"{subject[0].id},{subject[1].id}",  # format using = "1,2"
            "salary_grade": 2,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", form_data, format="multipart")
        assert response.status_code == status.HTTP_201_CREATED
        response_json = response.json()
        assert response_json["first_name"] == form_data["first_name"]
        assert response_json["last_name"] == form_data["last_name"]
        assert response_json["mobile_number"] == form_data["mobile_number"]

    def test_staff_update_api(self, api_client, admin_user_token, staff_factory, subject_factory):
        staff_user = staff_factory.create()
        subject = subject_factory.create_batch(2)
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
            "date_joined": fake.date(),
            "subjects": f"{subject[0].id},{subject[1].id}",  # format using = "1,2"
            "salary_grade": 2,
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{staff_user.id}/", form_data)
        assert response.status_code == status.HTTP_200_OK
        response_json = response.json()
        assert response_json["first_name"] == form_data["first_name"]
        assert response_json["last_name"] == form_data["last_name"]
        assert response_json["mobile_number"] == form_data["mobile_number"]
        assert type(response_json) == dict

    def test_staff_patch_api(self, api_client, admin_user_token, staff_factory, subject_factory):
        staff_user = staff_factory.create()
        subject = subject_factory.create_batch(2)
        fatch_data = {
            "first_name": "name update",
            "image": self.generate_photo(),
            "mobile_number": bd_number_generator(),
            "email": fake.email(),
            "is_active": False,
            "date_joined": fake.date(),
            "subjects": f"{subject[0].id},{subject[1].id}",  # format using = "1,2"
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{staff_user.id}/", fatch_data)
        assert response.status_code == status.HTTP_200_OK
        response_json = response.json()
        assert response_json["first_name"] == fatch_data["first_name"]
        assert response_json["mobile_number"] == fatch_data["mobile_number"]
        assert type(response_json) == dict

    def test_staff_delete_api(self, api_client, admin_user_token, staff_factory):
        staff_user = staff_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{staff_user.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
