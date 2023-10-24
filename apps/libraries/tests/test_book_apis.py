import io
import pytest
from PIL import Image
from faker import Faker
from rest_framework import status

fake = Faker()

pytestmark = pytest.mark.django_db


class TestBookModelViewSet:
    base_url = "/api/v1/books"

    def test_list_api(self, api_client, book_factory):
        book_factory.create_batch(15)
        response = api_client.get(f"{self.base_url}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 15
        assert len(response.data["results"]) == 10
        response = api_client.get(response.data["next"])
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 5
        assert type(response.data) == dict

    def test_retrieve_api(self, api_client, admin_user_token, book_factory):
        book = book_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.get(f"{self.base_url}/{book.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.json()) == dict

    def generate_photo(self):
        file = io.BytesIO()
        image = Image.new("RGBA", size=(100, 100), color=(155, 0, 0))
        image.save(file, "png")
        file.name = "test.png"
        file.seek(0)
        return file

    def test_create_api(self, api_client, admin_user_token, library_factory):
        form_data = {
            "library": library_factory.create().id,
            "writer_name": fake.name(),
            "name": fake.name(),
            "cover_image": self.generate_photo(),
            "pdf_file": self.generate_photo(),
            "page_number": 250,
            "publication": fake.name(),
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.post(f"{self.base_url}/", form_data)
        assert response.status_code == status.HTTP_201_CREATED
        response.data["library"] == form_data["library"]
        response.data["writer_name"] == form_data["writer_name"]
        response.data["name"] == form_data["name"]
        response.data["page_number"] == form_data["page_number"]
        response.data["publication"] == form_data["publication"]
        assert type(response.json()) == dict

    def test_update_api(self, api_client, admin_user_token, book_factory, library_factory):
        book = book_factory.create()
        form_data = {
            "library": library_factory.create().id,
            "writer_name": fake.name(),
            "name": fake.name(),
            "cover_image": self.generate_photo(),
            "pdf_file": self.generate_photo(),
            "page_number": 250,
            "publication": fake.name(),
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.put(f"{self.base_url}/{book.id}/", form_data)
        assert response.status_code == status.HTTP_200_OK
        response.data["library"] == form_data["library"]
        response.data["writer_name"] == form_data["writer_name"]
        response.data["name"] == form_data["name"]
        response.data["page_number"] == form_data["page_number"]
        response.data["publication"] == form_data["publication"]
        response.data["library"] != book.library
        response.data["writer_name"] != book.writer_name
        response.data["name"] != book.name
        response.data["page_number"] != book.page_number
        response.data["publication"] != book.publication
        assert type(response.json()) == dict

    def test_patch_update_api(self, api_client, admin_user_token, book_factory, library_factory):
        book = book_factory.create()
        form_data = {
            "writer_name": fake.name(),
            "name": fake.name(),
            "page_number": 250,
            "publication": fake.name(),
        }
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.patch(f"{self.base_url}/{book.id}/", form_data)
        assert response.status_code == status.HTTP_200_OK
        response.data["writer_name"] == form_data["writer_name"]
        response.data["name"] == form_data["name"]
        response.data["page_number"] == form_data["page_number"]
        response.data["publication"] == form_data["publication"]
        response.data["writer_name"] != book.writer_name
        response.data["name"] != book.name
        response.data["page_number"] != book.page_number
        response.data["publication"] != book.publication
        assert type(response.json()) == dict

    def test_delete_api(self, api_client, admin_user_token, book_factory):
        book = book_factory.create()
        jwt_token = admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token['access_token']}")
        response = api_client.delete(f"{self.base_url}/{book.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
