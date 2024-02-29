from django.shortcuts import render
from django.http import HttpResponse


def room(request):
    # return HttpResponse("room")
    return render(request,'room.html')

def home(request):
    # return HttpResponse("home")
    return render(request,'home.html')
