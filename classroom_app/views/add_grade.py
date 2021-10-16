"""
This class is used for containing views related to adding grades to StudentDetail model
"""
from classroom_app.models import StudentDetail
from rest_framework import generics
from api.serializers import StudentDetailPostGradeSerializer
from api.permissions import AdminOrTeacherOnly
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework import status
class AddGradeView(generics.UpdateAPIView):

    serializer_class = StudentDetailPostGradeSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [AdminOrTeacherOnly]

    def get_queryset(self):
        return StudentDetail.objects.all()

    def perform_update(self, serializer):
        pk = self.kwargs.get('pk')
        student_detail = StudentDetail.objects.get(pk=pk)

        grade_no = student_detail.grade_no
        # Here, we will get the grade and do calculations
        if grade_no == 0:
            student_detail.avg_grade = serializer.validated_data['grade']

        else:
            student_detail.avg_grade = (
                student_detail.avg_grade + serializer.validated_data['grade']) / 2
        grade_no += 1

        serializer.save(avg_grade=student_detail.avg_grade, grade_no=grade_no)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(status=status.HTTP_204_NO_CONTENT)
