from django.shortcuts import render
from django.http import HttpResponse


def polls(request):
    return HttpResponse("This is polls app")


# Create your views here.
