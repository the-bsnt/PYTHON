from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


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
    data['params']= 
    print(data)
    return JsonResponse(data)
