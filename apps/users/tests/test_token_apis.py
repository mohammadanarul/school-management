import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from apps.users.models import User
from apps.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestJWTToken:
    base_api_endpoint = "/api/v1/token"

    @pytest.mark.django_db
    def test_create_token(self, api_client, user_factory):
        user = user_factory.create()
        user_data = {"mobile_number": user.mobile_number, "password": "password123"}
        response = api_client.post(f"{self.base_api_endpoint}/", data=user_data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert type(response.data) == dict

    @pytest.mark.django_db
    def test_refresh_token(self, api_client, user_token):
        token = user_token
        response = api_client.post(
            f"{self.base_api_endpoint}/refresh/",
            {"refresh": token["refresh_token"]},
            format="json",
        )
        assert response.status_code == status.HTTP_200_OK
        assert type(response.data) == dict
