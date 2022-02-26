from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import time
import random

################### Example 1 ###################


def external_api(status: bool) -> bool:
    time.sleep(2)

    if status is True:
        return True
    return False


@api_view()
def demo_view(_):

    if external_api(random.choice([True, False])):
        return Response({"message": "External API Response!"})
    return Response({"message": "Something went wrong!"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

################### End of Example 1 ###################


################### Example 2 ###################

def external_api_2() -> bool:
    time.sleep(2)

    data = [{}, {"arr1": [1, 2, 3], "arr2":[4, 5, 6]}]

    response = {'status': 200, 'data': random.choice(data)}

    return response


@api_view()
def demo_view_2(_):

    response = external_api_2()
    print('Sending request to external api')

    if response.get('status') == 200:
        if result := response.get('data'):
            return Response(result)

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    return Response(None, status=status.HTTP_503_SERVICE_UNAVAILABLE)

################### End of Example 2 ###################


################### Example 3 ###################
import json


class ResponseObject:
    def __init__(self) -> None:
        time.sleep(2)
        self.status_code = random.choice([200, 500])
        self._data = random.choice([{}, {"arr1": [1, 2, 3], "arr2":[4, 5, 6]}])

    def json(self) -> dict:
        return json.loads(json.dumps(self._data))


@api_view()
def demo_view_3(_):
    response = ResponseObject()
    print('Sending request to external api')

    if response.status_code == 200:
        if result := response.json():
            return Response(result)

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    return Response(None, status=status.HTTP_503_SERVICE_UNAVAILABLE)

################### End of Example 3 ###################

################### Example 4 ###################


import requests


@api_view()
def demo_view_4(_):
    url = 'https://reqres.in/api/users/2'
    response = requests.get(url)

    if response.status_code == 200:
        if result := response.json():
            response_dict = {}
            data = result.get('data')

            response_dict['name'] = data.get(
                'first_name') + ' ' + data.get('last_name')
            response_dict['email'] = data.get('email')
            return Response(response_dict)
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    if response.status_code == 204:
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    return Response(None, status=status.HTTP_503_SERVICE_UNAVAILABLE)

################### End of Example 4 ###################
