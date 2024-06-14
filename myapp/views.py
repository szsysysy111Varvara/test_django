from django.http import HttpResponse, HttpRequest
from rest_framework import generics
from serializers.serializers import SubTaskCreateSerializer, SubTaskSerializer
from .models import SubTask


def greeting(request: HttpRequest):
    return HttpResponse("<h1>Hello! It's my first view!</h1>")

def hello_user(request: HttpRequest):
    return HttpResponse("<h1>Hello, Vlad!</h1>")

class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer

class SubTaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

