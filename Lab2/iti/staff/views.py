from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.

def list(req):
    return HttpResponse(req.path)

def insert(req):
    return JsonResponse({"id":1})

def update(req,id):
    return JsonResponse({"id":id})


def delete(req,id):
    return HttpResponseRedirect('/staff')
