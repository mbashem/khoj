from django.shortcuts import render, redirect

# Create your views here.

from django.http import  HttpResponse


def index(request):
    return render(request, 'ClusterIndex.html')

