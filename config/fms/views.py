from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index page for the FMS webapp.")