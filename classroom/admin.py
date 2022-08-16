from django.contrib import admin
from classroom.models import Classroom, Student
# Register your models here.
admin.site.register([Classroom,Student])