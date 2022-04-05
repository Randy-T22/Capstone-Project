from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


# Create your views here.

def home_view(request:HttpRequest)->render:
    return render(request, 'index.html')

