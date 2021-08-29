from rest_framework import permissions


class AdminOrTeacherOnly(permissions.BasePermission):
    """
    Object-level permission to only allow teachers of a student to edit.
    Assumes the model instance has an `owner` attribute.
    """
    message = 'Only admin or teacher can list and/or edit student detail.'

    def has_object_permission(self, request, view, obj):
        # Only teacher and/or admin user will be able to,
        # edit and/or list this view.
        is_staff = bool(request.user and request.user.is_staff)

        return obj.student.teacher.first_name == request.user.username or is_staff
