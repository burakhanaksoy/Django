from django.urls import path, include
from rest_framework.routers import DefaultRouter

from classroom_app.views.teachers import TeacherList, TeacherDetails, AddStudentView
from classroom_app.views.students import StudentList, StudentDetails
from classroom_app.views.student_details import StudentDetailView
from classroom_app.views.add_grade import AddGradeView

from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# For swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'details', StudentDetailView, basename='StudentDetail')

urlpatterns = [
    path('students/', StudentList.as_view()),
    path('students/<int:pk>/', StudentDetails.as_view()),

    path('students/', include(router.urls)),

    path('teachers/', TeacherList.as_view()),
    path('teachers/<int:pk>/', TeacherDetails.as_view()),
    path('teachers/<int:pk>/add-student/', AddStudentView.as_view()),

    path('students/details/<int:pk>/add-grade/', AddGradeView.as_view()),

    # For swagger
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
        cache_timeout=0), name='schema-swagger-ui')
]
