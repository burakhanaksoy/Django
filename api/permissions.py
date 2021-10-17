from rest_framework import permissions
from classroom_app.models import StudentDetail

class AdminOrTeacherOnly(permissions.BasePermission):
    """
    Object-level permission to only allow teachers of a student to edit.
    Assumes the model instance has an `owner` attribute.
    """
    message = 'Only admin or teacher can list and/or edit student detail.'

    def has_permission(self, request, view):
        # Only teacher and/or admin user will be able to,
        # edit and/or list this view.
        is_staff = bool(request.user and request.user.is_staff)

        return is_staff or str(request.user.groups.all().first()) == 'teacher'


class AdminOnly(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class AdminOrRelatedTeacherOnly(permissions.BasePermission):
    """
    Allows access only to admin users and/or the related teacher.
    """
    message = "Only admin or this student's teacher can add grade."

    def has_permission(self, request, view):
        is_staff = bool(request.user and request.user.is_staff)
        pk = view.kwargs.get('pk')
        student_detail = StudentDetail.objects.get(pk=pk)
        return is_staff or (student_detail.student.teacher.first_name.lower() == request.user.username.lower())
