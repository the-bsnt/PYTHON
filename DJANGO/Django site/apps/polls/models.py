from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


# * Here each model is child of class django.db.models.Model. thats why we put models.Model inside the bracket of class.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Marks(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    total_marks = models.IntegerField(default=100)
    pass_marks = models.IntegerField(default=40)

    def __str__(self):
        return str(self.total_marks)
