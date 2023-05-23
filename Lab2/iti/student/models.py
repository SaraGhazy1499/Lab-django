from django.db import models

from staff.models import Staff

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    age=models.IntegerField()
    track=models.CharField(max_length=20)
    student_staff=models.ForeignKey(Staff,on_delete=models.CASCADE)
