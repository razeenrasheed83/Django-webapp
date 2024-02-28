from django.shortcuts import render
from django.http import HttpResponse


def room(request):
    # return HttpResponse("room")
    render(request,'room.html')

def home(request):
    # return HttpResponse("home")
    render(request,'home.html')
