from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import *


@csrf_exempt
def api_home(request, *args, **kwargs):
    body = request.body  # byte strings of JSON data
    print(body)
    data = {}
    try:
        data = json.loads(body)  # strings of JSON data -> python dictionary

    except:
        pass
    print(data)
    print(request.headers)
    # data["headers"] = request.headers  # or request.META
    #!  error occurs when you try to convert a non-serializable object (like HttpHeaders) into JSON
    # request.headers is not regular python dictionary but object of HttpHeaders. So, have to be converted to dict first.
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type

    print(data)
    return JsonResponse(data)


def api_model(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data["title"] = model_data.title
        # data["content"] = model_data.content
        # data["price"] = model_data.price
        data = model_to_dict(
            model_data, fields=["id", "title", "content", "price"]
        )  # price is Decimal which is not serilizable
        data["price"] = int(model_data.price)

        print(data)
        json_data_str = json.dumps(data)
    return HttpResponse(json_data_str, headers={"content-type": "application/json"})


# * Here the process is automated by JsonResponse. JsonResponse converts the dict into Json String and set the content type to application/json and returns response.


# & DRF View
@api_view(["POST"])
def drf_view(request, *args, **kwargs):
    # if request.method != "POST":
    #     return Response({"detail": "GET not allowed "}, status=405)
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["title", "content"])
    return Response(data)
