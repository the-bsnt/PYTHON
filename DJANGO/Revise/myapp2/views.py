from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    return HttpResponse("hwllo this is index from app2")
