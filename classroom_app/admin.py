from django.contrib import admin
from.models import Student, StudentDetail, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(StudentDetail)
class StudentDetailAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Student)
# admin.site.register(StudentDetail)
# admin.site.register(Teacher)
