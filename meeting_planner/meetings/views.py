from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
# from django.forms import modelform_factory
from .models import Meeting
from .models import Room
# Create your views here.
from .forms import MeetingForm


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, "meetings/rooms_list.html", {"rooms": rooms})


# MeetingForm = modelform_factory(Meeting, exclude=[])
# def new(request):
#     if request.method == "POST":
#         form = MeetingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("welcome")
#     else:
#         form = MeetingForm()
#     return render(request, "meetings/new.html", {"form": form})



def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})