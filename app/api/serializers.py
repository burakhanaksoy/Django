from django.db.models.fields import CharField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from classroom_app.models import Teacher, Student, StudentDetail

from .serializer_functions import apply_validator
from .serializer_functions import validate_special_char
from .serializer_functions import validate_age
from .serializer_functions import validate_age_type
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
        if Teacher.objects.all():
            query_set = Teacher.objects.filter(students__id=object.id)
            if query_set:
                return [f"{t.first_name} {t.last_name}_{t.id}" for t in list(query_set)]
        return "N/A"


class StudentPostSerializer(StudentSimpleSerializer):
    """
        Customized serializer. Use this for only displaying purpose.
    """

    teacher = serializers.ListField(
        child=serializers.CharField(min_length=1), allow_empty=True, write_only=True, required=False)

    class Meta:
        model = Student
        read_only_fields = ['student_id']
        fields = ("first_name", "last_name", "age", "teacher")

    def validate(self, attrs):
        temp_dict = {k: v for k, v in attrs.items() if k != "teacher"}
        apply_validator(validate_special_char, temp_dict)

        teacher_ids = attrs.get('teacher')
        if teacher_ids is not None and teacher_ids:
            teacher_id_list = [str(t.id) for t in list(Teacher.objects.all())]
            for id in teacher_ids:
                if not id in teacher_id_list:
                    raise ValidationError(
                        detail="One of the teachers' id does not exist. Cannot create student.")

        is_duplicate = Student.objects.filter(first_name=attrs.get(
            'first_name')).filter(last_name=attrs.get('last_name')).filter(age=attrs.get('age'))
        if is_duplicate:
            raise ValidationError(detail="Duplicate student.")

        return attrs


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
    id=serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()
    avg_grade = serializers.SerializerMethodField()

    class Meta:
        model = StudentDetail
        exclude = ['grade_no', 'student']

    def get_id(self, object):
        return object.student.id
    def get_age(self, object):
        return object.student.age

    def get_name(self, object):
        return {'first_name': object.student.first_name, 'last_name': object.student.last_name}

    def get_course(self, object):
        course_list = []
        if teachers := object.student.teacher.all():
            for teacher in teachers:
                course_list.append(teacher.course)
        return course_list

    def get_teacher(self, object):
        teacher_list = []
        if teachers := object.student.teacher.all():
            for teacher in teachers:
                teacher_list.append(teacher.first_name +
                                    ' ' + teacher.last_name)
        return teacher_list

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
