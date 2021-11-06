from django.urls import path, include
from rest_framework.routers import DefaultRouter

from classroom_app.views.teachers import TeacherList, TeacherDetails
from classroom_app.views.students import StudentList, StudentDetails
from classroom_app.views.student_details import StudentDetailView
from classroom_app.views.add_grade import AddGradeView

router = DefaultRouter()
router.register(r'details', StudentDetailView, basename='StudentDetail')

urlpatterns = [
    path('students/', StudentList.as_view(), name='students'),
    path('students/<int:pk>/', StudentDetails.as_view(), name='students-pk'),

    path('students/<int:pk>/', include(router.urls)),
    # path('students/details/', StudentDetailList.as_view()),
    # path('students/<int:pk>/details/', StudentDetailRetrieve.as_view()),

    path('teachers/', TeacherList.as_view()),
    path('teachers/<int:pk>/', TeacherDetails.as_view()),

    path('students/details/<int:pk>/add-grade/', AddGradeView.as_view())
]
