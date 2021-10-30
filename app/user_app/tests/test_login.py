from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.authtoken.models import Token


class TestLogin(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = ''

    def test_login(self):
        user = User.objects.create_user(username="admin", password="admin")
        self.url = reverse('login')

        data = {
            'username': 'admin',
            'password': 'admin'
        }
        response = self.client.post(path=self.url, data=data, format='json')
        token = Token.objects.get(user=user).key

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('token'), token)

    def test_login_user_not_exist(self):
        self.url = reverse('login')
        data = {
            'username': 'admin',
            'password': 'admin'
        }
        response = self.client.post(path=self.url, data=data, format='json')

        self.assertEqual(response.status_code, 400)
