from rest_framework import permissions
from classroom_app.models import StudentDetail

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class AdminOrTeacherOnly(permissions.BasePermission):
    """
    Object-level permission to only allow teachers of a student to edit.
    Assumes the model instance has an `owner` attribute.
    """
    message = 'Only admin or teacher can edit student detail.'

    def has_permission(self, request, view):
        # Only teacher and/or admin user will be able to,
        # edit and/or list this view.
        is_staff = bool(request.user and request.user.is_staff)
        is_safe_method = request.method in SAFE_METHODS
        is_teacher_group = str(request.user.groups.all().first()) == 'teacher'

        return is_staff or is_teacher_group or is_safe_method


class AdminOnly(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        is_safe_method = request.method in SAFE_METHODS
        return bool(request.user and request.user.is_staff) or is_safe_method


class AdminOrRelatedTeacherOnly(permissions.BasePermission):
    """
    Allows access only to admin users and/or the related teacher.
    """
    message = "Only admin or this student's teacher can do this operation."

    def has_permission(self, request, view):
        is_staff = bool(request.user and request.user.is_staff)
        is_related_teacher = False
        if request.method not in ["GET", "POST"]:
            pk = view.kwargs.get('pk')
            student_detail = StudentDetail.objects.get(pk=pk)
            is_related_teacher = student_detail.student.teacher.first_name.lower(
            ) == request.user.username.lower()

        is_safe_method = request.method in SAFE_METHODS

        return is_staff or is_related_teacher or is_safe_method
