from http.client import HTTPResponse
from django.shortcuts import render


# Create your views here.
# request -> response
# action
#request handler

def say_Hello(request):
    return HTTPResponse("Hello World")