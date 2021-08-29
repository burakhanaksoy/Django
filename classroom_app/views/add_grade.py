"""
This class is used for containing views related to adding grades to StudentDetail model
"""
from classroom_app.models import StudentDetail
from rest_framework import generics
from api.serializers import StudentDetailPostGradeSerializer
from api.permissions import AdminOrTeacherOnly


class AddGradeView(generics.UpdateAPIView):

    serializer_class = StudentDetailPostGradeSerializer
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
