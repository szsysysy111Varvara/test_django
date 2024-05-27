from django.http import HttpResponse, HttpRequest

def greeting(request: HttpRequest):
    return HttpResponse("<h1>Hello! It's my first view!</h1>")

def hello_user(request: HttpRequest):
    return HttpResponse("<h1>Hello, Vlad!</h1>")


