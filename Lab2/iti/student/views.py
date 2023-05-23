from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def list(req):
   return HttpResponse(req.path)

def insert(r):
  return render(r,'student/add.html')

def update(r,id):
    return render(r,'student/edit.html')


def delete(req,id):
    return HttpResponseRedirect('/student')

