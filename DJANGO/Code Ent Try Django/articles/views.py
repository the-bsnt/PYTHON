from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def article_home(request):

    # from database???
    article_obj = Article.objects.get(pk=2)
    article_queryset = Article.objects.all()

    context = {
        "object_list": article_queryset,
        "article_name": article_obj.atitle,
        "article_content": article_obj.content,
    }

    return render(request, "home.html", context)


def article_search_view(request):

    query_dict = request.GET  # request.GET is a dictionary
    query = query_dict.get("q")
    if query is not None:
        context = {"article_obj": Article.objects.get(id=query)}
    return render(request, "search.html", context)
