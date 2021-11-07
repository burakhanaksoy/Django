from rest_framework.exceptions import APIException
from rest_framework import status


class NotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Document not exist.'
    default_code = 'invalid'
