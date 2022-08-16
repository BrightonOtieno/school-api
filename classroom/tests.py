from django.test import TestCase
from classroom.models import Student, Classroom
# Create your tests here.

# Testing MODELS
class TestStudent(TestCase):

    def test_student_can_be_created(self):

        student1 = Student.objects.create(
            first_name = 'John',
            last_name = 'terry',
            admission_number = 12345,
        ) 

        student_result =  Student.objects.last()

        self.assertEqual(student_result.first_name, "John")

        
    def test_str_return_value(self):

        student1 = Student.objects.create(
            first_name = 'John',
            last_name = 'terry',
            admission_number = 12345,
        ) 

        student_result =  Student.objects.last()

        self.assertEqual(student_result.first_name, "John")


    def test_get_grade_fail(self):

        student1 = Student.objects.create(
            first_name = 'John',
            last_name = 'terry',
            admission_number = 12345,
            average_score = 10
        ) 

        student_result =  Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Fail")


    def test_get_grade_pass(self):

        student1 = Student.objects.create(
            first_name = 'John',
            last_name = 'terry',
            admission_number = 12345,
            average_score = 45
        ) 

        student_result =  Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Pass")

    def test_get_grade_excellent(self):

        student1 = Student.objects.create(
            first_name = 'John',
            last_name = 'terry',
            admission_number = 12345,
            average_score = 75
        ) 

        student_result =  Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Excellent")





