from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Navya(request):
    return HttpResponse('<marquee><h1>My name is Navya sree</h1></marquee>')

def Course(request):
    return HttpResponse('<marquee><h1>Python Fullstack</h1></marquee>')