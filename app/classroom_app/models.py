
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.functional import empty
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

from django.contrib.auth.admin import UserAdmin

User.add_to_class('course', models.CharField(max_length=100))
UserAdmin.list_display += ('Extra Fields', {'fields': ('course',)})
UserAdmin.list_display = (
    'username', 'email', 'first_name', 'last_name', 'is_staff', 'course')
UserAdmin.fieldsets[0][1]['fields'] += ('course',)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, default='test@test.com')
    course = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.email = f'{self.user.first_name.lower()}.{self.user.last_name.lower()}{self.id}@school.com'
        if self.user.first_name:
            self.first_name = self.user.first_name
        if self.user.last_name:
            self.last_name = self.user.last_name
        if self.user.course:
            self.course = self.user.course
        if self.email.split('.')[0]:
            self.user.email = self.email

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Teacher {self.first_name}'


def create_user_profile(sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created']:
        teacher = Teacher(user=user)


post_save.connect(create_user_profile, sender=User)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.teacher.save()


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
