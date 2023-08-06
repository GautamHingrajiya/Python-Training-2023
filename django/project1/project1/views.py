from django.http import HttpResponse
from django.shortcuts import render


# def logIn(request):
#     return render(request , "index.html") 

def logIn(request):
    return render(request , "jobs.html") 


def aboutUs(request):
    return HttpResponse("Hello Gautam Welcome to Django Project")

def course(request):
    return HttpResponse("Hello Gautam Welcome to Django Course Page")

def coursenext(request,courseid):
    return HttpResponse(courseid)