from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.authtoken.models import Token


class TestLogout(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = ''
        self.user = User.objects.create_user(
            username="admin", password="admin")
        self.token = Token.objects.get(user=self.user).key

    def test_logout(self):
        self.url = reverse('logout')

        headers = {
            "HTTP_AUTHORIZATION": f"Token {self.token}",
            "Content-Type": "application/json"
        }
        response = self.client.post(
            path=self.url, format='json', **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('msg'), 'logout successfully.')

    def test_logout_invalid_token(self):
        self.url = reverse('logout')

        headers = {
            "HTTP_AUTHORIZATION": f"Token {self.token}1",
            "Content-Type": "application/json"
        }
        response = self.client.post(
            path=self.url, format='json', **headers)

        self.assertEqual(response.status_code, 401)
