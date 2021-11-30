from classroom_app.models import StudentDetail
from api.serializers import StudentDetailSerializer
from api.serializers import StudentGradeSerializer
from api.permissions import AdminOrRelatedTeacherOnly

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import generics
from rest_framework import filters


class StudentDetailView(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [AdminOrRelatedTeacherOnly]
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer

    # Use these if u use viewsets.ViewSet
    def list(self, request):
        """Overrides mixins.ListModelMixin list method """
        serializer = StudentDetailSerializer(
            StudentDetail.objects.all(), many=True)
        if not serializer.data:
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentDetailViewWithQuery(generics.ListAPIView):
    """
    List a queryset.
    """
    serializer_class = StudentDetailSerializer
    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        name = self.request.GET.get('name')
        queryset = StudentDetail.objects.all()

        if name and (result := queryset.filter(student__first_name__iexact=name)):
            return result

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        if serializer.data:
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = StudentDetail.objects.all()
    #     name = self.request.query_params.get('name')
    #     if name is not None:
    #         queryset = queryset.filter(
    #             student_detail__student__first_name=name)
    #     return queryset

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

class StudentGrades(generics.ListAPIView):
    serializer_class = StudentGradeSerializer
    queryset = StudentDetail.objects.all()
    authentication_classes = []
    permission_classes = []
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['avg_grade']
