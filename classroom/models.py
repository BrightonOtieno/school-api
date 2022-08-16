from re import M, T
from django.db import models

# Create your models here.



class Student(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    admission_number = models.IntegerField(unique=True)
    is_qualified = models.BooleanField(default=False)
    average_score = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.first_name 
    
    def get_grade(self):
        if self.average_score < 40:
            return "Fail"
        elif 40 < self.average_score > 70 :
            return "pass"
        elif (self.average_score > 70) :
            return "Excellent"
        
        else:
            return "Error"
class Classroom(models.Model):
    name = models.CharField(max_length=120)
    student_capacity = models.IntegerField()
    students = models.ManyToManyField("classroom.Student")

    def __str__(self):
        return self.name