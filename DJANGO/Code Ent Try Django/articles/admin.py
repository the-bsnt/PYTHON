from django.contrib import admin
from .models import *

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "atitle"]
    search_fields = ["atitle", "content"]


admin.site.register(Article, ArticleAdmin)
