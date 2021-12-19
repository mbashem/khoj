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
        
        # print(show_clusters_user)
        # print(request.user.username)

        return render(request, 'index.html', params)

    else:

        params = {'msg': 'login to view clusters'}
        return render(request, 'index.html', params)


def search_result(request):

    # received value through html form
    search_text = request.POST.get("search_text")
    Depth = (request.POST.get("depth"))
    UserName = request.POST.get("user_name")
    Cluster_Name = request.POST['selected_cluster']

    print(search_text)
    print(Depth)
    print(UserName)
    print(Cluster_Name)

    # query to get strategy list of the selected cluster

    obj_of_cluster = Clusters.objects.get(user_name=request.user.username, cluster_name=Cluster_Name)

    cluster_id = obj_of_cluster.cluster_id

    list_of_strategy = ClusterStrategy.objects.filter(cluster=cluster_id).values_list('strategy')

    print(list_of_strategy)


    # query to get url list of the selected cluster

    obj_of_cluster = Clusters.objects.get(user_name=request.user.username, cluster_name=Cluster_Name)

    cluster_id = obj_of_cluster.cluster_id

    list_of_urls = UrlList.objects.filter(cluster=cluster_id).values_list('url_name')

    print(list_of_urls)







