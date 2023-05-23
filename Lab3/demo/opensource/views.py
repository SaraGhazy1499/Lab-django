from django.http import HttpResponse
from django.shortcuts import render
from opensource.models import Track , Student
# Create your views here.


def home(req):
    return HttpResponse("<h1>This is home page</h1>")


def getStudent(req,st_id):
    st=Student.objects.get(id=st_id)
    context={'student':st}
    return render(req,'opensource/student_details.html',context)


def getAllStudents(req):
    all_students=Student.objects.all()
    context={'students':all_students}
    return render(req,'opensource/student.html',context)


