from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# employee management;


class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.d_name


class Employee(models.Model):
    e_id = models.AutoField(primary_key=True)
    e_name = models.CharField(max_length=50, unique=True)
    e_email = models.CharField(max_length=50, unique=True)
    d_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.e_name


# to study forms
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default="fallback.png", blank=True)

    def __str__(self):
        return self.title
