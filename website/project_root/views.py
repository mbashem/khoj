import os

from django.shortcuts import render, redirect
from django.db import connection, connections

from django.core.exceptions import ObjectDoesNotExist

from auth_app import *

from django.http import  HttpResponse
from CreateClusters.models import *
from auth_app.models import *

def index(request):

    if request.user.is_authenticated:
        show_clusters_user =  Clusters.objects.filter( user_name=request.user.username).values_list('cluster_name', 'depth', 'isScrapedCluster')

        params = {'Query': show_clusters_user, 'msg': 'here are your clusters!'}
        
        print(show_clusters_user)
        print(request.user.username)
    

        return render(request, 'index.html', params)
    else:
        print("else part execute")
        params = {'msg': 'login to view clusters'}
        return render(request, 'index.html', params)


