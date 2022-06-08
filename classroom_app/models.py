
from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, default='test@test.com')
    course = models.CharField(max_length=100)

    def __str__(self):
        return f'Teacher ID: {self.id}'


class Student(models.Model):
    # id = models.AutoField(primary_key=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    teacher = models.OneToOneField(Teacher, primary_key=True,
                                   on_delete=models.DO_NOTHING, related_name='student')

    def __str__(self):
        return f'Student: {self.first_name}'


class StudentDetail(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='student'
    )
    # teacher = models.ManyToManyField(
    #     Teacher, related_name='teacher')
    city = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=12,
                             blank=True, unique=True, null=True)
    grade = models.PositiveIntegerField(default=0)
    avg_grade = models.FloatField(default=0)
    grade_no = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Student Details"

    def __str__(self):
        return f'{self.student_id}'
