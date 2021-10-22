from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
 return HttpResponse("this is the demo of a shop")
