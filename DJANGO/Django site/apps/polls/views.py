from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.http import Http404


# displays the latest 5 poll questions in the system,
def index(request):
    question_list = Question.objects.order_by("-pub_date")[:5]
    return render(request, "polls/index.html", {"questions": question_list})


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)  # shortcut
    return render(request, "polls/detail.html", {"question": question})



