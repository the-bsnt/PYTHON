from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse


def index(request):
    question_list = Question.objects.all()
    return render(request, "index.html", {"questions": question_list})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "myapp/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST.get("choice"))
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "myapp/detail.html",
            {
                "question": question,
                "error_message": "Either You didn't select a choice",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("myapp:results", args=(question_id,)))


def search(request):
    q = request.GET.get("q")
    print(request.GET)
    print(q)
    return HttpResponse("this is WSGI request")
