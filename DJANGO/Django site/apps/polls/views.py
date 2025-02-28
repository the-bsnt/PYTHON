from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# displays the latest 5 poll questions in the system,

"""def index(request):
    question_list = Question.objects.order_by("-pub_date")[:5]
    return render(request, "polls/index.html", {"questions": question_list})"""

# Using class based generic views


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)  # shortcut
    return render(request, "polls/detail.html", {"question": question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     choice_id = request.POST["option"]
#     selected_choice = question.choice_set.get(pk=choice_id)
#     selected_choice.votes = F("votes") + 1
#     selected_choice.save()


#     return HttpResponseRedirect(reverse("polls:results", args=(question_id)))
def vote(request, question_id):
    print("everything al right")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        # return render(request, "polls/results.html", {"question": question})


def results(request, question_id):
    print("this is ", request.method)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

    # here, we use post->redirect->get (PRG) pattern.
