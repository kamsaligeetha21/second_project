from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_first(request):
    return HttpResponse('<h1>first file in app2</h1>')


def app2_second(request):
    return HttpResponse('<h1>second file in app2</h1>')