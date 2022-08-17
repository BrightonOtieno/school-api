from django.test import TestCase
from mixer.backend.django import mixer
from classroom.models import Student, Classroom
# Create your tests here.

# Testing MODELS
class TestStudent(TestCase):

    def setUp(self):
        self.student1 = Student.objects.create(
            first_name = 'John',
            last_name = 'terry',
            admission_number = 12345,
        ) 

    def test_student_can_be_created(self):
        # with pytest 
        # assert self.student1.first_name == "John"

        self.assertEqual(self.student1.first_name, "John")



        
    def test_str_return_value(self):

        self.assertEqual(self.student1.first_name, "John")


    def test_get_grade_fail(self):
        # student1 = Student.objects.create(
        #     first_name = 'John',
        #     last_name = 'terry',
        #     admission_number = 123451,
        #     average_score = 30
        # )

        student1 = mixer.blend(Student, average_score=30)

        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Fail")


    def test_get_grade_pass(self):

        # student1 = Student.objects.create(
        #     first_name = 'John',
        #     last_name = 'terry',
        #     admission_number = 1234,
        #     average_score = 45
        # )

        student1 = mixer.blend(Student, average_score= 45)

        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Pass")

    def test_get_grade_excellent(self):
        # student1 = Student.objects.create(
        #     first_name = 'John',
        #     last_name = 'terry',
        #     admission_number = 12346,
        #     average_score = 100
        # )


        student1 = mixer.blend(Student, average_score=100)

        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Excellent")





