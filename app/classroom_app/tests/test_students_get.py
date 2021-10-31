from classroom_app.models import Student, Teacher
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
import json


class TestStudentsGet(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = ''

    def test_204_no_students(self):
        self.url = reverse('students')
        response = self.client.get(path=self.url)

        self.assertEqual(response.status_code, 204)

    def test_200(self):
        self.url = reverse('students')
        teacher = {
            "first_name": "test_teacher",
            "last_name": "test",
            "course": "CS101"
        }
        teacher = Teacher.objects.create(**teacher)
        teacher_pk = teacher.pk

        student = {
            "first_name": "Burak",
            "last_name": "Aksoy",
            "age": 26,
            "teacher": Teacher.objects.get(pk=teacher_pk)
        }
        Student.objects.create(**student)

        response = self.client.get(path=self.url)

        self.assertEqual(response.status_code, 200)
