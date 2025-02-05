from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def room(request):
    context = {
        "rooms": [
            {"id": 1, "msg": "Lets learn python"},
            {"id": 2, "msg": "Design database with me"},
            {"id": 3, "msg": "Analysis data with me"},
        ]
    }
    return render(request, "testapp/room.html", context)


rooms_detail = [
    {"id": 1, "owner": "basnet", "location": "right corner"},
    {"id": 2, "owner": "hari", "location": "middle"},
    {"id": 3, "owner": "prabesh", "location": "left corner"},
]


def room_detail(request, id):

    for room in rooms_detail:
        if room["id"] == int(id):
            return render(request, "testapp/room_detail.html", room)
    return HttpResponse("room not found")
