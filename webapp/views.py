from django.shortcuts import render
from django.http import HttpResponse


def webapp(request):
    return HttpResponse("Hello world!")
