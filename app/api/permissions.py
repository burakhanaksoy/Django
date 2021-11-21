from rest_framework import permissions
from classroom_app.models import StudentDetail, Student
from classroom_app.errors import raise_not_found_with_status

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
        is_teacher_group = str(request.user.groups.all().first()) == 'Teachers'

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
            try:
                teacher_email_list = []
                # group_name_list = map(
                #     extract_group_names, list(request.user.groups.all()))

                if any(group.name == "Teachers" for group in list(request.user.groups.all())):

                    if student_detail := StudentDetail.objects.get(pk=pk):
                        teachers = student_detail.student.teacher.all()

                    for teacher in list(teachers):
                        teacher_email_list.append(teacher.email)

                    if request.user.email in teacher_email_list:
                        is_related_teacher = True
                else:
                    is_related_teacher = False

                ####
                # user_group_list = list(request.user.groups.all())
                # if any(user_group in user_group_list for user_group in  )
                """
                Burada sey yapcam,
                    1- request.user'in eklendigi gruplarin ismini bir listede topla
                    2- Bu isim listesi icinde "Teachers"'i bulmaya calis
                    3- Bulursan bil ki o user ogretmendir...
                """
                ###

            except StudentDetail.DoesNotExist:
                self.message = 'Student does not exist.'
                raise_not_found_with_status(self.message)

        is_safe_method = request.method in SAFE_METHODS

        return is_staff or is_related_teacher or is_safe_method
