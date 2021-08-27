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
        read_only_fields = ['id']
        exclude = ['id', 'email']

    def validate(self, attrs):
        temp_dict = {k: v for k, v in attrs.items() if (
            k != "email" and k != "course")}
        apply_validator(validate_special_char, temp_dict)

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
    teacher = TeacherSimpleSerializer(read_only=False)

    class Meta:
        model = Student
        read_only_fields = ['student_id']
        fields = '__all__'


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
    info = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    # teacher = TeacherSimpleSerializer(read_only=False, many=True)

    class Meta:
        model = StudentDetail
        fields = '__all__'
        # exclude = ['student']

    def get_age(self, object):
        return object.student.age

    def get_info(self, object):
        return {'first_name': object.student.first_name, 'last_name': object.student.last_name}

    def validate(self, attrs):
        temp_dict = {k: v for k, v in attrs.items() if (
            k != "email" and k != "student")}
        apply_validator(validate_special_char, temp_dict)
        if 'email' in attrs.keys():
            validate_email(attrs.get("email"))
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
