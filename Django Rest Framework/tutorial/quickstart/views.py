from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


@api_view(["GET"])
def get_user(request):
    return Response(UserSerializer({"username": "sdfs", "age": 34}).data)
