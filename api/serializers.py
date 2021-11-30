from django.db.models.fields import CharField
from rest_framework import serializers
from classroom_app.models import Teacher, Student, StudentDetail

from .serializer_functions import apply_validator
from .serializer_functions import validate_special_char
from .serializer_functions import validate_age
from .serializer_functions import validate_email
from classroom_app.models import Student


class TeacherSimpleSerializer(serializers.ModelSerializer):
    """
        Teacher simple serializer. Use this for POST, PUT operations
    """
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ['id']
        optional_fields = ['email', ]

    def validate(self, attrs):
        temp_dict = {k: v for k, v in attrs.items() if (
            k != "email" and k != "course")}
        apply_validator(validate_special_char, temp_dict)
        attrs["email"] = f"{attrs.get('first_name','test').lower()}.{attrs.get('last_name','test').lower()}@school.com"

        if("email" in attrs.keys()):
            validate_email(attrs.get("email"))
        return attrs


class TeacherWithOnlyCoursesGivenFieldSerializer(TeacherSimpleSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSimpleSerializer(serializers.ModelSerializer):
    """
        Student simple serializer. Use this for POST, PUT operations
    """
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, attrs):
        temp_dict = {k: v for k, v in attrs.items() if k != "teacher"}
        apply_validator(validate_special_char, temp_dict)
        if("age" in attrs.keys()):
            validate_age(attrs.get('age'))
        return attrs


class StudentListSerializer(StudentSimpleSerializer):
    """
        Customized serializer. Use this for only displaying purpose.
    """
    teacher = serializers.SerializerMethodField()

    class Meta:
        model = Student
        read_only_fields = ['student_id']
        fields = '__all__'

    def get_teacher(self, object):
        return {"name": f'{object.teacher.first_name} {object.teacher.last_name}', "course": object.teacher.course}


class StudentPostSerializer(StudentSimpleSerializer):
    """
        Customized serializer. Use this for only displaying purpose.
    """

    class Meta:
        model = Student
        read_only_fields = ['student_id']
        fields = '__all__'


class StudentTeacherDiscardedSerializer(StudentSimpleSerializer):

    class Meta:
        model = Student
        read_only_fields = ['student_id']
        # fields = '__all__'
        exclude = ["teacher"]


class StudentSerializerUpdate(StudentSimpleSerializer):
    """
        Customized serializer. Use this for only displaying purpose.
    """
    class Meta:
        model = Student
        read_only_fields = ['student_id']
        exclude = ['first_name', 'last_name', 'age']


class StudentDetailSerializer(serializers.ModelSerializer):
    """
        Student Detail Serializer base.
    """
    name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()
    avg_grade = serializers.SerializerMethodField()

    class Meta:
        model = StudentDetail
        exclude = ['grade_no']

    def get_age(self, object):
        return object.student.age

    def get_name(self, object):
        return {'first_name': object.student.first_name, 'last_name': object.student.last_name}

    def get_course(self, object):
        return object.student.teacher.course

    def get_teacher(self, object):
        return object.student.teacher.first_name + ' ' + object.student.teacher.last_name

    def get_grade(self, object):
        return object.grade

    def get_avg_grade(self, object):
        return object.avg_grade

    def validate(self, attrs):
        temp_dict = {k: v for k, v in attrs.items() if (
            k != "email" and k != "student" and k != "grade" and k != "avg_grade")}
        apply_validator(validate_special_char, temp_dict)
        if 'email' in attrs.keys():
            validate_email(attrs.get("email"))
        return attrs


class StudentDetailPostGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields = ('grade', 'city', 'email', 'avg_grade', 'grade_no')

    def validate(self, attrs):
        if attrs['grade'] < 0:
            raise serializers.ValidationError(
                {"grade": "Grade cannot be negative."})
        return attrs


class StudentDetailSerializerWithTeacherFieldSerializer(StudentDetailSerializer):
    teacher = TeacherSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = StudentDetail
        fields = '__all__'


class TeacherWithStudentFieldSerializer(serializers.ModelSerializer):
    # teacher_student = StudentListSerializer(many=True, read_only=True)
    # students = serializers.SerializerMethodField()
    student = StudentTeacherDiscardedSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'

    # def get_students(self, object):
    #     return object


class StudentGradeSerializer(serializers.ModelSerializer):
    """
        Student Detail Serializer base.
    """
    name = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()
    avg_grade = serializers.SerializerMethodField()

    class Meta:
        model = StudentDetail
        exclude = ['city', 'email', 'phone', 'student']

    def get_name(self, object):
        return object.student.first_name + ' ' + object.student.last_name

    def get_course(self, object):
        return object.student.teacher.course

    def get_grade(self, object):
        return object.grade

    def get_avg_grade(self, object):
        return object.avg_grade

    def validate(self, attrs):
        temp_dict = {k: v for k, v in attrs.items() if (
            k != "email" and k != "student" and k != "grade" and k != "avg_grade")}
        apply_validator(validate_special_char, temp_dict)
        if 'email' in attrs.keys():
            validate_email(attrs.get("email"))
        return attrs
