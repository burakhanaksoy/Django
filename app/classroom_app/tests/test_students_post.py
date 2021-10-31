from classroom_app.models import Teacher
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User


class TestStudentsPost(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('students')

    def test_201_created_no_teacher(self):
        self.user = User.objects.create_superuser(username="test")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "Aksoy",
            "age": 26
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get(
            'first_name'), data.get('first_name'))
        self.assertEqual(response.data.get('last_name'), data.get('last_name'))
        self.assertEqual(response.data.get('age'), data.get('age'))

    def test_201_created_with_empty_teacher_field(self):
        self.user = User.objects.create_superuser(username="test")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "Aksoy",
            "age": 26,
            "teacher": []
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get(
            'first_name'), data.get('first_name'))
        self.assertEqual(response.data.get('last_name'), data.get('last_name'))
        self.assertEqual(response.data.get('age'), data.get('age'))

    def test_201_created_with_non_empty_teacher_field(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        Teacher.objects.create(first_name="test_teacher2")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "Aksoy",
            "age": 26,
            "teacher": [1, 2]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get(
            'first_name'), data.get('first_name'))
        self.assertEqual(response.data.get('last_name'), data.get('last_name'))
        self.assertEqual(response.data.get('age'), data.get('age'))

    def test_400_with_adding_non_existing_teacher_id(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        Teacher.objects.create(first_name="test_teacher2")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "Aksoy",
            "age": 26,
            "teacher": [3]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 400)

    def test_400_with_adding_multiple_teacher_and_one_non_existing_teacher_id(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        Teacher.objects.create(first_name="test_teacher2")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "Aksoy",
            "age": 26,
            "teacher": [1, 2, 3]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 400)

    def test_400_with_student_first_name_less_than_2_char(self):
        self.user = User.objects.create_superuser(username="test")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "B",
            "last_name": "Aksoy",
            "age": 26
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 400)

    def test_201_with_student_first_name_equals_2_char(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Bu",
            "last_name": "Aksoy",
            "age": 26,
            "teacher": [1]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 201)

    def test_400_with_student_last_name_less_than_2_char(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "A",
            "age": 26,
            "teacher": [1]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 400)

    def test_201_with_student_last_name_equals_2_char(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "Ak",
            "age": 26,
            "teacher": [1]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 201)

    def test_400_with_student_age_less_than_18(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "Ak",
            "age": 17,
            "teacher": [1]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 400)

    def test_400_with_student_age_equals_18(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "Ak",
            "age": 18,
            "teacher": [1]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 201)

    def test_400_with_student_age_greater_than_55(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "Ak",
            "age": 56,
            "teacher": [1]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 400)

    def test_201_with_student_age_equals_55(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "Ak",
            "age": 55,
            "teacher": [1]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 201)

    def test_400_special_char_in_first_name(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan@",
            "last_name": "Ak",
            "age": 26,
            "teacher": [1]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 400)

    def test_400_special_char_in_last_name(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "Ak@",
            "age": 26,
            "teacher": [1]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 400)

    def test_400_with_age_float(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "Ak",
            "age": 26.5,
            "teacher": [1]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 400)

    def test_400_with_age_str(self):
        self.user = User.objects.create_superuser(username="test")
        Teacher.objects.create(first_name="test_teacher")
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "Burakhan",
            "last_name": "Ak",
            "age": "26s",
            "teacher": [1]
        }

        response = self.client.post(path=self.url, data=data)

        self.assertEqual(response.status_code, 400)



    
