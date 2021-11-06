from classroom_app.models import Student, Teacher
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse


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
        teacher_data = {
            "first_name": "test_teacher",
            "last_name": "test",
            "course": "CS101"
        }
        teacher = Teacher.objects.create(**teacher_data)
        teacher_pk = teacher.pk

        student_data = {
            "first_name": "Burak",
            "last_name": "Aksoy",
            "age": 26
        }
        student = Student.objects.create(**student_data)
        student.teacher.add(Teacher.objects.get(pk=teacher_pk))

        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, 200)

    def test_200_student_have_multiple_teacher(self):
        self.url = reverse('students')
        teacher1_data = {
            "first_name": "test_teacher",
            "last_name": "test",
            "course": "CS101"
        }

        teacher2_data = {
            "first_name": "test_teacher2",
            "last_name": "test2",
            "course": "CS102"
        }

        Teacher.objects.create(**teacher1_data)
        Teacher.objects.create(**teacher2_data)

        student_data = {
            "first_name": "Burak",
            "last_name": "Aksoy",
            "age": 26
        }
        student = Student.objects.create(**student_data)
        student.teacher.add(Teacher.objects.get(pk=1))
        student.teacher.add(Teacher.objects.get(pk=2))

        response = self.client.get(path=self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0].get("id"), 1)
        self.assertEqual(response.data[0].get("age"), 26)
        self.assertEqual(response.data[0].get("first_name"), "Burak")
        self.assertEqual(response.data[0].get("last_name"), "Aksoy")
        self.assertTrue( "test_teacher test_1" in response.data[0].get("teacher"))
        self.assertTrue( "test_teacher2 test2_2" in response.data[0].get("teacher"))
