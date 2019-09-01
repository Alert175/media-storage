from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello world!!!!!</h1>")


def user(request):
    return HttpResponse("<h2>this is users page</h2>")


def user_name(request, user_name="incognito"):
    return HttpResponse("<h1>Hello {name}!</h1>".format(name=user_name))

