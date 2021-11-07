from rest_framework.response import Response
from rest_framework import status
from api.exceptions import NotFoundError
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def return_400_with_error_log(msg):
    logging.error(f"ERROR: Returned 400")
    logging.error(msg)
    return Response(None, status=status.HTTP_400_BAD_REQUEST)


def return_404_with_error_log():
    logging.error(f"ERROR: Returned 404")
    logging.error('Not Found')
    return Response(None, status=status.HTTP_404_NOT_FOUND)


def return_400_admin_error():
    logging.error(f"ERROR: Returned 400")
    logging.error('Only admin can make this change')
    return Response('Only admin can make this change', status=status.HTTP_400_BAD_REQUEST)


def raise_not_found_with_status(msg):
    raise NotFoundError(msg)
