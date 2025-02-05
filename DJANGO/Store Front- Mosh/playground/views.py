from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("hello world")


def calculate():
    x = 1
    y = 2
    return x + y


def base(request):
    x = calculate()
    content = {"name": "basnet sameer"}
    return render(request, "base.html", content)


# in views function we can do following:
#   -pull data from the database
#   -update or transform the data in database
#   -send email,etc
