from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
import json


expected_responses = {
    "user_create_success": {
        'username': 'test_user',
        'email': 'test@test.com',
        'first_name': 'test',
        'last_name': 'test'
    },
    "same_username_different_email_error": {
        "errors": {
            "username": ["A user with that username already exists."]
        }
    },
    "different_username_same_email": {"errors": {"email": ["This field must be unique."]}},
    "password_forgotten": {"errors": {"password2": ["This field is required."]}},
    "password_mismatch": {"errors": {"password": ["Password fields didn't match."]}},
    "first_name_not_given": {"errors": {"first_name": ["This field is required."]}}
}


class TestAccountCreate(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = ''

    def test_user_create(self):
        self.url = reverse('register')
        data = {
            "username": "test_user",
            "email": "test@test.com",
            "password": "testtest1234",
            "password2": "testtest1234",
            "first_name": "test",
            "last_name": "test"
        }
        response = self.client.post(self.url, data=data, format='json')
        if response.data.get('token'):
            generated_token = response.data.pop('token')
        else:
            generated_token = None

        expected_result = expected_responses.get('user_create_success')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, expected_result)
        self.assertIsNotNone(generated_token)

    def test_user_create_same_username_different_email_error(self):
        User.objects.create(username="test_user")

        self.url = reverse('register')
        data = {
            "username": "test_user",
            "email": "test1@test.com",
            "password": "testtest1234",
            "password2": "testtest1234",
            "first_name": "test",
            "last_name": "test"
        }
        response = self.client.post(self.url, data=data, format='json')

        expected_result = json.dumps(expected_responses.get(
            'same_username_different_email_error'))

        result = json.dumps(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(result, expected_result)

    def test_user_create_different_username_same_email_error(self):
        User.objects.create(username="foo", email="test@test.com")

        self.url = reverse('register')
        data = {
            "username": "test_user1",
            "email": "test@test.com",
            "password": "testtest1234",
            "password2": "testtest1234",
            "first_name": "test",
            "last_name": "test"
        }
        response = self.client.post(self.url, data=data, format='json')

        expected_result = json.dumps(expected_responses.get(
            'different_username_same_email'))

        result = json.dumps(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(result, expected_result)

    def test_user_create_password2_not_entered(self):
        self.url = reverse('register')
        data = {
            "username": "test_user1",
            "email": "test@test.com",
            "password": "testtest1234",
            "first_name": "test",
            "last_name": "test"
        }
        response = self.client.post(self.url, data=data, format='json')

        expected_result = json.dumps(expected_responses.get(
            'password_forgotten'))

        result = json.dumps(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(result, expected_result)

    def test_user_create_passwords_mismatch(self):

        self.url = reverse('register')
        data = {
            "username": "test_user",
            "email": "test1@test.com",
            "password": "testtest12345",
            "password2": "testtest1234",
            "first_name": "test",
            "last_name": "test"
        }
        response = self.client.post(self.url, data=data, format='json')

        expected_result = json.dumps(expected_responses.get(
            'password_mismatch'))

        result = json.dumps(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(result, expected_result)

    def test_user_create_first_name_not_given(self):

        self.url = reverse('register')
        data = {
            "username": "test_user",
            "email": "test1@test.com",
            "password": "testtest12345",
            "password2": "testtest1234",
            "last_name": "test"
        }
        response = self.client.post(self.url, data=data, format='json')

        expected_result = json.dumps(expected_responses.get(
            'first_name_not_given'))

        result = json.dumps(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(result, expected_result)   
