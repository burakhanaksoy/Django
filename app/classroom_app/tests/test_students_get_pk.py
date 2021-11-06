from classroom_app.models import Student, Teacher
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User


class TestStudentsPost(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('students')

    def test_401_authorization_not_provided(self):
        response = self.client.get(path=f"{self.url}1/")

        self.assertEqual(response.status_code, 401)

    def test_404_no_student(self):
        self.user = User.objects.create(username="test")
        self.client.force_authenticate(user=self.user)

        response = self.client.get(path=f"{self.url}1/")
        self.assertEqual(response.status_code, 404)

    def test_200_no_teacher(self):
        Student.objects.create(first_name="Burakhan",
                               last_name="Aksoy", age=19)
        self.user = User.objects.create_user(username="test")
        self.client.force_authenticate(user=self.user)

        response = self.client.get(path=f"{self.url}1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('first_name'), "Burakhan")
        self.assertEqual(response.data.get('last_name'), "Aksoy")
        self.assertEqual(response.data.get('age'), 19)
        self.assertEqual(response.data.get('teacher'), "N/A")

    def test_200_multiple_teachers(self):
        teacher_1 = Teacher.objects.create(
            first_name="test", last_name="test", course="CStest")
        teacher_2 = Teacher.objects.create(
            first_name="test2", last_name="test2", course="CStest")
        student = Student.objects.create(first_name="Burakhan",
                                         last_name="Aksoy", age=19)
        student.teacher.add(teacher_1)
        student.teacher.add(teacher_2)

        self.user = User.objects.create_user(username="test")
        self.client.force_authenticate(user=self.user)

        response = self.client.get(path=f"{self.url}1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('first_name'), "Burakhan")
        self.assertEqual(response.data.get('last_name'), "Aksoy")
        self.assertEqual(response.data.get('age'), 19)
        self.assertIn(
            f'test test_{teacher_1.id}', response.data.get('teacher'))
        self.assertIn(
            f'test2 test2_{teacher_2.id}', response.data.get('teacher'))

