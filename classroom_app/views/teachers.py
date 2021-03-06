from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from classroom_app.models import Teacher
from rest_framework.exceptions import ValidationError
from api.serializers import TeacherSimpleSerializer, TeacherWithStudentFieldSerializer
from classroom_app.errors import return_400_with_error_log, return_404_with_error_log, return_400_admin_error
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
    def get(self, request, format=None):
        teachers = Teacher.objects.all()
        data = TeacherWithStudentFieldSerializer(teachers, many=True).data
        result = dict()
        result['result'] = data
        if result['result']:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(responses={201: "CREATED"}, request_body=TeacherSimpleSerializer())
    def post(self, request, format=None):
        serializer = TeacherSimpleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Returned 201")
            logging.info(f'INFO: {request.data} created')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return return_400_with_error_log(serializer.errors)


class TeacherDetails(APIView):
    """
    Retrieve, update or delete a Student instance.
    """

    def get(self, request, pk, format=None):
        data = {}
        data_list = []
        try:
            teacher = Teacher.objects.get(pk=pk)

        except Teacher.DoesNotExist:
            return return_404_with_error_log()

        if teacher:
            data = TeacherSimpleSerializer(teacher).data
        else:
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        data_list.append(data)

        result = dict()
        result['result'] = data_list

        return Response(result, status=200)

    def put(self, request, pk, format=None):
        is_super_user = self.request.user.is_superuser
        if not is_super_user:
            raise ValidationError('Only Admin account can do this operation.')

        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSimpleSerializer(teacher, data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Patched successfully")
            logging.info(f'INFO: {request.data} updated')
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        return return_400_with_error_log(serializer.errors)

    def patch(self, request, pk, format=None):
        is_super_user = self.request.user.is_superuser
        if not is_super_user:
            raise ValidationError('Only Admin account can do this operation.')

        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSimpleSerializer(teacher, data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Patched successfully")
            logging.info(f'INFO: {request.data} updated')
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        return return_400_with_error_log(serializer.errors)

    def delete(self, request, pk, format=None):
        is_super_user = self.request.user.is_superuser
        if not is_super_user:
            raise ValidationError('Only Admin account can do this operation.')
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return return_404_with_error_log()
        teacher.delete()
        logging.info(f"INFO: Deleted successfully")
        logging.info(f'INFO: {teacher} deleted')
        return Response(None, status=status.HTTP_204_NO_CONTENT)
