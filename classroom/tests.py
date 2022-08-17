
# from django.test import TestCase
from unicodedata import name
import pytest
from mixer.backend.django import mixer
from hypothesis import strategies as st , given
from hypothesis.extra.django import TestCase
from classroom.models import Student, Classroom
# Create your tests here.
pytestmark = pytest.mark.django_db
# Testing MODELS
class TestStudent(TestCase):

    # def setUp(self):
    #     self.student1 = Student.objects.create(
    #         first_name = 'John',
    #         last_name = 'terry',
    #         admission_number = 12345,
    #     ) 

    def test_student_can_be_created(self):
        student1 = Student.objects.create(
            first_name = 'John',
            last_name = 'terry',
            admission_number = 123451,
            average_score = 30
        )
        # with pytest 
        # assert self.student1.first_name == "John"

        # self.assertEqual(self.student1.first_name, "John")

        assert student1.first_name == "John"



        
    def test_str_return_value(self):
        student1 = mixer.blend(Student, first_name = 'John')
        # self.assertEqual(str(self.student1), "John")
        assert student1.first_name == "John"

    @given(st.text())
    def test_slugify(self, username):
        """ Fails on Unicodes, emojis"""
        print("username", username)

        student1 = mixer.blend(Student, first_name=username)
        student1.save()
        student_result = Student.objects.last()
        assert len(str(student_result.username)) ==  len(username)


    @given(st.floats(min_value=0, max_value=39))
    def test_get_grade_fail(self, fail_score):
        # student1 = Student.objects.create(
        #     first_name = 'John',
        #     last_name = 'terry',
        #     admission_number = 123451,
        #     average_score = 30
        # )

        student1 = mixer.blend(Student, average_score=fail_score)
    

        student_result = Student.objects.last()

        # self.assertEqual(student_result.get_grade(), "Fail")
        assert student_result.get_grade() ==  "Fail"

    @given(st.floats(min_value=40, max_value=69))
    def test_get_grade_pass(self, pass_score):

        # student1 = Student.objects.create(
        #     first_name = 'John',
        #     last_name = 'terry',
        #     admission_number = 1234,
        #     average_score = 45
        # )

        student1 = mixer.blend(Student, average_score=pass_score)

        student_result = Student.objects.last()

        assert student_result.get_grade() ==  "Pass"

    @given(st.floats(min_value=70, max_value=99))
    def test_get_grade_excellent(self, excellent_score):
        # student1 = Student.objects.create(
        #     first_name = 'John',
        #     last_name = 'terry',
        #     admission_number = 12346,
        #     average_score = 100
        # )


        student1 = mixer.blend(Student, average_score=excellent_score)

        student_result = Student.objects.last()

        assert student_result.get_grade() ==  "Excellent"

    @given(st.floats(min_value=100))
    def test_get_grade_error(self, error_score):
        # student1 = Student.objects.create(
        #     first_name = 'John',
        #     last_name = 'terry',
        #     admission_number = 12346,
        #     average_score = 100
        # )


        student1 = mixer.blend(Student, average_score=error_score)

        student_result = Student.objects.last()

        assert student_result.get_grade() ==  "Error"


class TestClassroomModel:

    def test_classroom_can_be_created(self):

        classroom = mixer.blend(Classroom, name="physics", student_capacity=3)
        classroom_result = Classroom.objects.last()
        assert str(classroom_result) == "physics"






