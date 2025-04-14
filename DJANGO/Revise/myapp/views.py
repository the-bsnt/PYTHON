from django.shortcuts import render

from django.http import HttpResponse
from .models import *


def index(request):
    question_list = Question.objects.all()
    return render(request, "index.html", {"questions": question_list})


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, "myapp/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
