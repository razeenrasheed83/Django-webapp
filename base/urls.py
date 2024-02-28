from django.urls import path
from .import views

urlpatterns = [
    path('',views.room,name="room"),
    path('index/',views.index,name="index")
]
