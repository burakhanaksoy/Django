from classroom_app.models import StudentDetail
from rest_framework.response import Response
from rest_framework import status
from api.serializers import StudentDetailSerializerWithTeacherFieldSerializer, StudentDetailSerializer
from rest_framework.views import APIView
import logging
from classroom_app.errors import return_400_with_error_log, return_400_admin_error, return_404_with_error_log
from rest_framework.exceptions import ValidationError
from api.access_policies import StudentDetailAccessPolicy, StudentDetailDeleteAccessPolicy
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import authentication, permissions

from api.permissions import AdminOrTeacherOnly, AdminOnly


class StudentDetailView(viewsets.ModelViewSet):
    """
    View for displaying student detail information.
    [
        {
            "student": 1,
            "info": {
                "first_name": "Burakhan",
                "last_name": "Aksoy"
            },
            "age": 26,
            "course": "CS101",
            "teacher": "Ahmet Cevdet",
            "grade": 0,
            "avg_grade": 0.0,
            "city": "Istanbul",
            "email": "burakhan.aksoy@test.com",
            "phone": "218382181221"
        }
    ]
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [AdminOrTeacherOnly]
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer

# Use these if u use viewsets.ViewSet
    def list(self, request):
        """Overrides mixins.ListModelMixin list method """
        serializer = StudentDetailSerializer(self.queryset, many=True)
        if not serializer.data:
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # def retrieve(self, request, pk=None):
    #     queryset = StudentDetail.objects.all()
    #     detail = get_object_or_404(queryset, pk=pk)
    #     serializer = StudentDetailSerializer(detail)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     # if not request.user.username == 'admin':
    #     #     return return_400_admin_error()
    #     serializer = StudentDetailSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         logging.info(f"INFO: Returned 201")
    #         logging.info(f'INFO: {request.data} created')
    #         return Response(None, status=status.HTTP_201_CREATED)
    #     else:
    #         return return_400_with_error_log(serializer.errors)

    # def destroy(self, request):
    #     pass

    # def get(self, request, pk, format=None):
    #     data = {}
    #     try:
    #         student_detail = StudentDetail.objects.get(pk=pk)
    #     except StudentDetail.DoesNotExist:
    #         return return_404_with_error_log()

    #     if student_detail:
    #         serializer = StudentDetailSerializer(student_detail)
    #     else:
    #         return Response(None, status=status.HTTP_204_NO_CONTENT)

    #     return Response(serializer.data, status=200)

    # def put(self, request, pk, format=None):
    #     is_super_user = self.request.user.is_superuser
    #     if not is_super_user:
    #         raise ValidationError('Only Admin account can do this operation.')
    #     detail_object = StudentDetail.objects.get(pk=pk)
    #     serializer = StudentDetailSerializer(
    #         detail_object, data=request.data, partial=False)

    #     if serializer.is_valid():
    #         serializer.save()
    #         logging.info(f"INFO: Patched successfully")
    #         logging.info(f'INFO: {request.data} updated')
    #         return Response(None, status=status.HTTP_200_OK)
    #     else:
    #         return return_400_with_error_log(serializer.errors)

    # def patch(self, request, pk):
    #     is_super_user = self.request.user.is_superuser
    #     if not is_super_user:
    #         raise ValidationError('Only Admin account can do this operation.')

    #     detail_object = StudentDetail.objects.get(pk=pk)
    #     # set partial=True to update a data partially
    #     serializer = StudentDetailSerializer(
    #         detail_object, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(None, status=status.HTTP_200_OK)
    #     return return_400_with_error_log(serializer.errors)

    # def delete(self, request, pk, format=None):
    #     try:
    #         student_detail = StudentDetail.objects.get(pk=pk)
    #     except StudentDetail.DoesNotExist:
    #         return return_404_with_error_log()
    #     student_detail.delete()
    #     logging.info(f"INFO: Deleted successfully")
    #     logging.info(f'INFO: {student_detail} deleted')
    #     return Response(None, status=status.HTTP_204_NO_CONTENT)


# class StudentDetailList(APIView):
#     # permission_classes = (StudentDetailAccessPolicy,)

#     def post(self, request, format=None):
#         if not request.user.username == 'admin':
#             return return_400_admin_error()
#         serializer = StudentDetailSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             logging.info(f"INFO: Returned 201")
#             logging.info(f'INFO: {request.data} created')
#             return Response(None, status=status.HTTP_201_CREATED)
#         else:
#             return return_400_with_error_log(serializer.errors)
