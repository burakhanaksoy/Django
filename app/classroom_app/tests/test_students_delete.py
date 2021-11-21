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
        user = User.objects.create_user(
            username="ahmet")
        user.first_name = "Ahmet"
        user.last_name = "Mentese"
        user.course = "CS101"
        user.save()

        user.groups.add(self.teacher_group)
        teacher = Teacher.objects.filter(email="ahmet.mentese1@school.com")[0]
        student = Student.objects.create(
            first_name="test", last_name="test", age=19)
        student.teacher.add(teacher)
        StudentDetail.objects.create(student=student)

        self.client.force_authenticate(user=user)

        response = self.client.delete(path=f"{self.url}1/")

        self.assertEqual(response.status_code, 204)

    def test_204_multiple_teachers_related_teacher_can_delete_successfully(self):
        teacher_1 = User.objects.create_user(
            username="ahmet")
        teacher_1.first_name = "Ahmet"
        teacher_1.last_name = "Mentese"
        teacher_1.course = "BIO101"
        teacher_1.save()

        teacher_2 = User.objects.create_user(
            username="ibrahim")
        teacher_2.first_name = "Ibrahim"
        teacher_2.last_name = "Sonmez"
        teacher_2.course = "CS403"
        teacher_2.save()

        teacher_3 = User.objects.create_user(
            username="polat")
        teacher_3.first_name = "Polat"
        teacher_3.last_name = "Alemdar"
        teacher_3.course = "PHIL103"
        teacher_3.save()

        teacher_1.groups.add(self.teacher_group)
        teacher_2.groups.add(self.teacher_group)
        teacher_3.groups.add(self.teacher_group)

        student = Student.objects.create(
            first_name="test", last_name="test", age=19)

        student.teacher.add(Teacher.objects.all()[0])
        student.teacher.add(Teacher.objects.all()[1])
        student.teacher.add(Teacher.objects.all()[2])

        StudentDetail.objects.create(student=student)

        self.client.force_authenticate(user=teacher_2)

        response = self.client.delete(path=f"{self.url}1/")

        self.assertEqual(response.status_code, 204)

    def test_403_multiple_teachers_unrelated_teacher_gets_403(self):
        teacher_1 = User.objects.create_user(
            username="ahmet")
        teacher_1.first_name = "Ahmet"
        teacher_1.last_name = "Mentese"
        teacher_1.course = "BIO101"
        teacher_1.save()

        teacher_2 = User.objects.create_user(
            username="ibrahim")
        teacher_2.first_name = "Ibrahim"
        teacher_2.last_name = "Sonmez"
        teacher_2.course = "CS403"
        teacher_2.save()

        teacher_3 = User.objects.create_user(
            username="polat")
        teacher_3.first_name = "Polat"
        teacher_3.last_name = "Alemdar"
        teacher_3.course = "PHIL103"
        teacher_3.save()

        teacher_1.groups.add(self.teacher_group)
        teacher_2.groups.add(self.teacher_group)
        teacher_3.groups.add(self.teacher_group)

        student = Student.objects.create(
            first_name="test", last_name="test", age=19)

        student.teacher.add(Teacher.objects.all()[0])
        student.teacher.add(Teacher.objects.all()[2])

        StudentDetail.objects.create(student=student)

        self.client.force_authenticate(user=teacher_2)

        response = self.client.delete(path=f"{self.url}1/")

        self.assertEqual(response.status_code, 403)
