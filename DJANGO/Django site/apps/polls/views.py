from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# displays the latest 5 poll questions in the system,
def index(request):
    question_list = Question.objects.order_by("-pub_date")[:5]
    # question_list is queryset, so convert it into list first
    # print(question_list)
    output = str(list(question_list))
    # output = ", ".join(str(list(question_list)))
    return HttpResponse(output)


def polls(request):
    return HttpResponse("This is polls app")
