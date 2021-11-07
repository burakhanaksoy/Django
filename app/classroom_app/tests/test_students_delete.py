from classroom_app.models import Student, Teacher, StudentDetail
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class TestStudentsDelete(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('students')
        self.teacher_group, _ = Group.objects.get_or_create(name="Teachers")

    def test_401_authorization_not_provided(self):
        user = User.objects.create(username="test")
        student = Student.objects.create(
            first_name="test", last_name="test", age=19)
        StudentDetail.objects.create(
            student=student)

        response = self.client.delete(path=f"{self.url}1/")

        self.assertEqual(response.status_code, 401)

    def test_403_no_permission(self):
        user = User.objects.create(first_name="test")
        student = Student.objects.create(
            first_name="test", last_name="test", age=19)

        StudentDetail.objects.create(
            student=student)

        self.client.force_authenticate(user=user)

        response = self.client.delete(path=f"{self.url}1/")

        self.assertEqual(response.status_code, 403)

    def test_404_document_not_exist_authenticated_with_admin(self):
        user = User.objects.create_superuser(username="admin")

        self.client.force_authenticate(user=user)
        response = self.client.delete(path=f"{self.url}1/")

        self.assertEqual(response.status_code, 404)

    def test_204_admin_can_delete_successfully(self):
        user = User.objects.create_superuser(username="test")
        student = Student.objects.create(
            first_name="test", last_name="test", age=19)
        StudentDetail.objects.create(student=student)

        self.client.force_authenticate(user=user)

        response = self.client.delete(path=f"{self.url}1/")

        self.assertEqual(response.status_code, 204)
        self.assertTrue(list(Student.objects.all()) == [])

    def test_204_related_teacher_can_delete_successfully(self):
        teacher = User.objects.create_user(
            username="ahmet", email="ahmet.mentese@school.com")
        teacher.groups.add(self.teacher_group)

        student = Student.objects.create(
            first_name="test", last_name="test", age=19)
        student.teacher.add(Teacher.objects.create(
            first_name="Ahmet", last_name="Mentese", email="ahmet.mentese@school.com", course="CS101"))
        StudentDetail.objects.create(student=student)

        self.client.force_authenticate(user=teacher)

        response = self.client.delete(path=f"{self.url}1/")

        self.assertEqual(response.status_code, 204)

    def test_204_multiple_teachers_related_teacher_can_delete_successfully(self):
        teacher_1 = User.objects.create_user(
            username="ahmet", email="ahmet.mentese@school.com")
        teacher_2 = User.objects.create_user(
            username="ibrahim", email="ibrahim.sonmez@school.com")
        teacher_3 = User.objects.create_user(
            username="polat", email="polat.alemdar@school.com")

        teacher_1.groups.add(self.teacher_group)
        teacher_2.groups.add(self.teacher_group)
        teacher_3.groups.add(self.teacher_group)

        student = Student.objects.create(
            first_name="test", last_name="test", age=19)

        student.teacher.add(Teacher.objects.create(
            first_name="Ahmet", last_name="Mentese", email="ahmet.mentese@school.com", course="CS101"))
        student.teacher.add(Teacher.objects.create(
            first_name="Ibrahim", last_name="Sonmez", email="ibrahim.sonmez@school.com", course="CS101"))
        student.teacher.add(Teacher.objects.create(
            first_name="Polat", last_name="Alemdar", email="polat.alemdar@school.com", course="CS101"))

        StudentDetail.objects.create(student=student)

        self.client.force_authenticate(user=teacher_2)

        response = self.client.delete(path=f"{self.url}1/")

        self.assertEqual(response.status_code, 204)

    def test_403_multiple_teachers_unrelated_teacher_gets_403(self):
        teacher_1 = User.objects.create_user(
            username="ahmet", email="ahmet.mentese@school.com")
        teacher_2 = User.objects.create_user(
            username="ibrahim", email="ibrahim.sonmez@school.com")
        teacher_3 = User.objects.create_user(
            username="polat", email="polat.alemdar@school.com")

        teacher_1.groups.add(self.teacher_group)
        teacher_2.groups.add(self.teacher_group)
        teacher_3.groups.add(self.teacher_group)

        student = Student.objects.create(
            first_name="test", last_name="test", age=19)

        student.teacher.add(Teacher.objects.create(
            first_name="Ahmet", last_name="Mentese", email="ahmet.mentese@school.com", course="CS101"))
        student.teacher.add(Teacher.objects.create(
            first_name="Polat", last_name="Alemdar", email="polat.alemdar@school.com", course="CS101"))

        StudentDetail.objects.create(student=student)

        self.client.force_authenticate(user=teacher_2)

        response = self.client.delete(path=f"{self.url}1/")

        self.assertEqual(response.status_code, 403)
