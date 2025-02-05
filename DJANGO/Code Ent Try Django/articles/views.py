from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def article_home(request):
    article_obj = Article.objects.get(pk=2)
    context = {
        "article_name": article_obj.title,
        "article_content": article_obj.content,
    }

    return render(request, "home.html", context)
