from requests.api import request
from rest_framework.test import APISimpleTestCase
from rest_framework.test import APIClient
from django.urls import reverse

from unittest.mock import patch

# Create your tests here.


class TestDemoView(APISimpleTestCase):
    client = APIClient()
    url = reverse('demo_view')

    @patch('demo_app.views.external_api')
    def test_200_external(self, mock_obj):
        mock_obj.return_value = True
        response = self.client.get(self.url)

        assert response.data == {'message': 'External API Response!'}

    @patch('demo_app.views.external_api')
    def test_503_external(self, mock_obj):
        mock_obj.return_value = False
        response = self.client.get(self.url)

        assert response.data == {"message": "Something went wrong!"}


class TestDemoView_2(APISimpleTestCase):
    client = APIClient()
    url = reverse('demo_view_2')

    def test_200_external(self):
        with patch('demo_app.views.external_api_2') as external_api_mock:
            external_api_mock.return_value = {
                'status': 200,
                'data': {"arr1": [1, 2, 3], "arr2": [4, 5, 6]}
            }
            response = self.client.get(self.url)

        assert response.status_code == 200
        assert response.data == {'arr1': [1, 2, 3], 'arr2': [4, 5, 6]}

    def test_204_external(self):
        with patch('demo_app.views.external_api_2') as external_api_mock:
            external_api_mock.return_value = {
                'status': 200,
                'data': {}
            }
            response = self.client.get(self.url)

        assert response.status_code == 204
        assert response.data is None

    def test_503_external(self):
        with patch('demo_app.views.external_api_2') as external_api_mock:
            external_api_mock.return_value = {
                'status': 500,  # Here, we need to return any other status code than 200
                'data': {}
            }
            response = self.client.get(self.url)

        assert response.status_code == 503
        assert response.data is None

################### UT 3 ###################


import json


class ResponseObjectMock:
    def __init__(self, status_code, data) -> None:
        self.status_code = status_code
        self._data = data

    def json(self) -> dict:
        return json.loads(json.dumps(self._data))


class TestDemoView_3(APISimpleTestCase):
    client = APIClient()
    url = reverse('demo_view_3')

    def test_200_external(self):
        with patch('demo_app.views.ResponseObject') as mock_object:
            mock_object.return_value = ResponseObjectMock(
                status_code=200, data={'key': "this is some data"})
            response = self.client.get(self.url)

        assert response.status_code == 200
        assert response.data == {'key': 'this is some data'}

    def test_204_external(self):
        with patch('demo_app.views.ResponseObject') as mock_object:
            mock_object.return_value = ResponseObjectMock(
                status_code=200, data={})
            response = self.client.get(self.url)

        assert response.status_code == 204
        assert response.data is None

    def test_503_external(self):
        with patch('demo_app.views.ResponseObject') as mock_object:
            mock_object.return_value = ResponseObjectMock(
                status_code=500, data={})
            response = self.client.get(self.url)

        assert response.status_code == 503
        assert response.data is None

################## End of UT 3 ###################

################### UT 4 ###################


from unittest.mock import Mock
from requests.exceptions import Timeout
import requests


def response_200(*args, **kwargs):
    mock_obj = Mock()
    mock_obj.status_code = 200
    mock_obj.json.return_value = {
        'data': {
            'first_name': "Burakhan",
            'last_name': "Aksoy",
            'email': "burak@burak.com"
        }
    }
    return mock_obj


def response_204(*args, **kwargs):
    mock_obj = Mock()
    mock_obj.status_code = 204
    return mock_obj


def response_500(*args, **kwargs):
    mock_obj = Mock()
    mock_obj.status_code = 500
    return mock_obj


@patch('demo_app.views.requests')
class TestDemoView_4(APISimpleTestCase):
    client = APIClient()
    url = reverse('demo_view_4')

    def test_200_external(self, request_mock):
        request_mock.get.side_effect = response_200
        response = self.client.get(self.url)

        self.assertEqual(response.data, {
            'name': 'Burakhan Aksoy', 'email': 'burak@burak.com'})
        self.assertEqual(response.status_code, 200)

    def test_200_external(self, request_mock):
        request_mock.get.side_effect = response_204
        response = self.client.get(self.url)

        self.assertIsNone(response.data)
        self.assertEqual(response.status_code, 204)

    def test_503_external_raise_error(self, request_mock):
        request_mock.get.side_effect = response_500
        response = self.client.get(self.url)

        self.assertIsNone(response.data)
        self.assertEqual(response.status_code, 503)

    def test_with_retry(self, request_mock):
        request_mock.get.side_effect = [response_500(), response_200()]
        response = self.client.get(self.url)

        self.assertIsNone(response.data)
        self.assertEqual(response.status_code, 503)

        response = self.client.get(self.url)

        self.assertEqual(response.data, {
            'name': 'Burakhan Aksoy', 'email': 'burak@burak.com'})
        self.assertEqual(response.status_code, 200)

# import unittest
# import json
# from requests.exceptions import Timeout
# from unittest.mock import Mock

# json = Mock()


# def first_fn(*args, **kwargs):
#     if response := json.loads():
#         return response

#     # return json.loads()

# # def second_fn(*args, **kwargs):
# #     print('inside second function')
#     # json.loads()


# class TestSideEffect(unittest.TestCase):

#     def test_1(self):
#         json.loads.side_effect = [Timeout, {'response': 'json loads response'}]

#         with self.assertRaises(Timeout) as e:
#             first_fn()

#         r = first_fn()
#         self.assertEqual(r, {'response': 'json loads response'})
#         # result = first_fn('some args', kwarg='some kwarg')
#         # print(json.loads())

# # json.loads('arg1', 'arg2', kwarg_1='kwarg1', kwarg_2='kwarg2')

# # def first_fn(*args, **kwargs):
# #     json.loads.return_value = 1

# # def second_fn(*args, **kwargs):
# #     print('inside second function')
# #     return

# # json = Mock()
# # json.loads.side_effect = [first_fn, second_fn]

################### End of UT 4 ###################
