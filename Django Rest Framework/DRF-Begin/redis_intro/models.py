from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField()
    hs_code = models.CharField(max_length=6)
    price = models.FloatField(default=0.0)
