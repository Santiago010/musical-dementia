"views chat"

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(
        request=request,
        template_name='chat/index.html'
    )


def room(request,room_name):
    return render(
        request=request,
        template_name='chat/room.html',
        context={
            'room_name' : room_name
        }
    )