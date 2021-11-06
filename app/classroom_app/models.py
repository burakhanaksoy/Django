
from django.db import models
from django.utils.functional import empty
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, default='test@test.com')
    course = models.CharField(max_length=100)

    def __str__(self):
        return f'Teacher {self.first_name}'


class Student(models.Model):
    first_name = models.CharField(
        validators=[MinLengthValidator(2)], max_length=50)
    last_name = models.CharField(
        validators=[MinLengthValidator(2)], max_length=50)
    age = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(55)])
    teacher = models.ManyToManyField(
        Teacher, related_name='students', blank=True)

    def __str__(self):
        return f'Student {self.first_name}'


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

    def __str__(self):
        return f'{self.student_id}'
