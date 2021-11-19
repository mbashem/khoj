from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse


def index(request):
    return render(request, 'ClusterIndex.html')

def withoutLogin(request):
    return render(request, 'index.html')