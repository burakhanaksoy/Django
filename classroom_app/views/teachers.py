from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from classroom_app.models import Teacher

from api.serializers import (TeacherSimpleSerializer,
                             TeacherWithStudentFieldSerializer,
                             TeacherUpdateSerializer,
                             AddStudentSerializer)
from classroom_app.errors import return_400_with_error_log, return_404_with_error_log
import logging
from api.permissions import AdminOrTeacherOnly
from rest_framework import authentication
from drf_yasg.utils import swagger_auto_schema


class TeacherList(APIView):
    """
    List all teachers, or create a new teacher.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (AdminOrTeacherOnly,)

    @swagger_auto_schema(responses={200: TeacherWithStudentFieldSerializer(many=True)})
    def get(self, _):
        teachers = Teacher.objects.all()
        serializer = TeacherWithStudentFieldSerializer(teachers, many=True)

        if not serializer.data:
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={201: "CREATED"}, request_body=TeacherSimpleSerializer())
    def post(self, request):
        serializer = TeacherSimpleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Returned 201")
            logging.info(f'INFO: {request.data} created')
            return Response(status=status.HTTP_201_CREATED)
        return return_400_with_error_log(serializer.errors)


class TeacherDetails(APIView):
    """
    Retrieve, update or delete a Student instance.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (AdminOrTeacherOnly,)

    def get(self, _, pk):
        data = {}

        try:
            teacher = Teacher.objects.get(pk=pk)

        except Teacher.DoesNotExist:
            return return_404_with_error_log()

        if teacher:
            data = TeacherWithStudentFieldSerializer(teacher).data
        else:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        return Response(data, status=200)

    def patch(self, request, pk):

        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherUpdateSerializer(
            teacher, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Patched successfully")
            logging.info(f'INFO: {request.data} updated')
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        return return_400_with_error_log(serializer.errors)

    def delete(self, _, pk):

        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return return_404_with_error_log()

        teacher.delete()
        logging.info(f"INFO: Deleted successfully")
        logging.info(f'INFO: {teacher} deleted')
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class AddStudentView(APIView):
    """Adding student to a specific teacher."""

    """
    body:(For existing students)
    {
        "existing":true,
        "student":[2]
    }

    body:(For newly created student, only one student!)

    {
        "name":"some",
        "surname":"student",
        "age":23
    }

    returns:
        HTTP_201_CREATED, 
        HTTP_400_BAD_REQUEST,
        HTTP_404_NOT_FOUND
    """

    def post(self, request, pk):
        existing = request.data.get('existing', False)
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return return_404_with_error_log()

        if not existing:
            request.data['teacher'] = []
            request.data['teacher'].append(teacher.id)
            serializer = AddStudentSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(data=None, status=status.HTTP_201_CREATED)
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
        else:
            students = request.data.get('student')
            try:
                teacher.student.add(*students)
            except Exception as e:
                print(e)
                return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
            return Response(data=None, status=status.HTTP_201_CREATED)
