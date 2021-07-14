from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Meeting
from .models import Room
# Create your views here.

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, "meetings/rooms_list.html", {"rooms": rooms})