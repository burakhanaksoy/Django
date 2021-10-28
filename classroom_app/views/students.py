from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from classroom_app.models import Student, StudentDetail
from rest_framework.exceptions import ValidationError
from api.serializers import StudentDetailSerializer, StudentListSerializer, StudentSerializerUpdate, StudentPostSerializer
from classroom_app.errors import return_400_with_error_log, return_404_with_error_log, return_400_admin_error
import logging
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import authentication, permissions

from api.permissions import AdminOrTeacherOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
class StudentList(APIView):
    """
    Method: POST,
    Query: Body
       {
        "first_name": "Burakhan",
        "last_name": "Aksoy",
        "age": 26,
        "teacher": 1 (PK of the Teacher)
        }
    """
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminOrTeacherOnly]

    def get(self, _, format=None):
        students = Student.objects.all()
        serializer = StudentListSerializer(students, many=True)

        if not serializer.data:
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # is_super_user = self.request.user.is_superuser
        # if not is_super_user:
        #     raise ValidationError('Only Admin account can do this operation.')
        serializer = StudentPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Returned 201")
            logging.info(f'INFO: {request.data} created')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return return_400_with_error_log(serializer.errors)


class StudentDetails(APIView):

    def get(self, request, pk, format=None):
        data = {}
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return return_404_with_error_log()

        if student:
            serializer = StudentListSerializer(student)
        else:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        is_super_user = self.request.user.is_superuser
        if not is_super_user:
            raise ValidationError('Only Admin account can do this operation.')
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializerUpdate(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Patched successfully")
            logging.info(f'INFO: {request.data} updated')
            return Response(None, status=status.HTTP_200_OK)
        else:
            return return_400_with_error_log(serializer.errors)

    def delete(self, request, pk, format=None):
        is_super_user = self.request.user.is_superuser
        if not is_super_user:
            raise ValidationError('Only Admin account can do this operation.')
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return return_404_with_error_log()
        student.delete()
        logging.info(f"INFO: Deleted successfully")
        logging.info(f'INFO: {student} deleted')
        return Response(None, status=status.HTTP_204_NO_CONTENT)
