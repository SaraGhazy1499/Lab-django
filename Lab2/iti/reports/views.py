from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def listStudent(req):
    return JsonResponse({"id":1})

def listStaff(req):
    return JsonResponse({"id":1})


def mainRepo(r):
    return render(r,'reports/main.html')




