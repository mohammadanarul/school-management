import pytest
import io
from PIL import Image
from rest_framework import status
from faker import Faker
from apps.helpers.helpers import bd_number_generator

pytestmark = pytest.mark.django_db

fake = Faker()


class TestInstituteModelViewSet:
    base_url = "/api/v1/institutes"

    def test_institute_list_api(self, api_client, admin_user_token, institute_factory):
        institute_factory.create_batch(13)
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

    def test_institute_retrieve_api(self, api_client, institute_factory):
        intitute = institute_factory.create()
        response = api_client.get(f"{self.base_url}/{intitute.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def generate_photo(self):
        file = io.BytesIO()
        image = Image.new("RGBA", size=(100, 100), color=(155, 0, 0))
        image.save(file, "png")
        file.name = "test.png"
        file.seek(0)
        return file

    def test_institute_create_api(self, api_client, admin_user_token):
        form_data = {
            "name": fake.name(),
            "established_year": fake.year(),
            "president": fake.name(),
            "principal": fake.name(),
            "website_domain_address": fake.url(),
            "email": fake.email(),
            "address": fake.address(),
            "phone_number_1": bd_number_generator(),
            "phone_number_2": bd_number_generator(),
            "image": self.generate_photo(),
            "logo": self.generate_photo(),
            "eiin_number": fake.random_int(),
            "institute_code": fake.random_int(),
            "institute_type": 1,
            "institute_about": fake.text(),
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", form_data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_institute_update_api(self, api_client, admin_user_token, institute_factory):
        intitute = institute_factory.create()
        form_data = {
            "name": fake.name(),
            "established_year": fake.year(),
            "president": fake.name(),
            "principal": fake.name(),
            "website_domain_address": fake.url(),
            "email": fake.email(),
            "address": fake.address(),
            "phone_number_1": bd_number_generator(),
            "phone_number_2": bd_number_generator(),
            "image": self.generate_photo(),
            "logo": self.generate_photo(),
            "eiin_number": fake.random_int(),
            "institute_code": fake.random_int(),
            "institute_type": 1,
            "institute_about": fake.text(),
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{intitute.id}/", form_data, format="multipart")
        assert response.status_code == status.HTTP_200_OK
        response_data = response.json()
        assert response_data["name"] == form_data["name"]
        assert response_data["established_year"] == int(form_data["established_year"])
        assert response_data["email"] == form_data["email"]
        assert response_data["address"] == form_data["address"]
        assert response_data["name"] != intitute.name
        assert response_data["principal"] != intitute.principal
        assert response_data["email"] != intitute.email
        assert response_data["address"] != intitute.address

    def test_institute_patch_update_api(self, api_client, admin_user_token, institute_factory):
        intitute = institute_factory.create()
        form_data = {
            "name": fake.name(),
            "principal": fake.name(),
            "email": fake.email(),
            "address": fake.address(),
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{intitute.id}/", form_data, format="multipart")
        print("bad_request_error:", response.data)
        assert response.status_code == status.HTTP_200_OK
        response_data = response.json()
        assert response_data["name"] == form_data["name"]
        assert response_data["principal"] == form_data["principal"]
        assert response_data["email"] == form_data["email"]
        assert response_data["address"] == form_data["address"]
        assert response_data["name"] != intitute.name
        assert response_data["principal"] != intitute.principal
        assert response_data["email"] != intitute.email
        assert response_data["address"] != intitute.address

    def test_institute_delete_api(self, api_client, admin_user_token, institute_factory):
        intitute = institute_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{intitute.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
