from classroom_app.models import Student, Teacher
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User


class TestStudentsDetails(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('students')

    # def test_401_unauthorized(self):

    #     response = self.client.get(path=f'{self.url}1/details/')
    #     self.assertEqual(response.status_code, 401)
