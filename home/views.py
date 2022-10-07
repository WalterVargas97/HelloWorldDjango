from http.client import TEMPORARY_REDIRECT
from re import TEMPLATE
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello WORLD. YOU ARE IN HOME")


