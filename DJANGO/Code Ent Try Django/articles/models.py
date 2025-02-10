from django.db import models


# Create your models here.
class Article(models.Model):
    atitle = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.atitle
