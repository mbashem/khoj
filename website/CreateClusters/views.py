from django.shortcuts import render, redirect

# Create your views here.

from django.http import  HttpResponse


def index(request):
<<<<<<< HEAD
    return render(request, 'ClusterIndex.html')
=======
    return render(request, 'CreateClusters/ClusterIndex.html')
>>>>>>> omi

