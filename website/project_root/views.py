import os

from django.shortcuts import render, redirect
from django.db import connection, connections

from django.core.exceptions import ObjectDoesNotExist

from auth_app import *

from django.http import  HttpResponse
from CreateClusters.models import *
from auth_app.models import *
from indexer.query import *

from indexer.IndexResult import *

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
        Cluster_Name = request.POST.get("selected_cluster")

        # print(search_text)
        # print(Depth)
        # print(UserName)
        # print(Cluster_Name)

        # query to get strategy list of the selected cluster

        obj_of_cluster = Clusters.objects.get(user_name=request.user.username, cluster_name=Cluster_Name)

        cluster_id = obj_of_cluster.cluster_id

        list_of_strategy = list(ClusterStrategy.objects.filter(cluster=cluster_id).values_list('strategy', flat=True))


        print(list_of_strategy)


        # query to get url list of the selected cluster

        obj_of_cluster = Clusters.objects.get(user_name=request.user.username, cluster_name=Cluster_Name)

        cluster_id = obj_of_cluster.cluster_id

        list_of_urls = list(UrlList.objects.filter(cluster=cluster_id).values_list('url_name', flat=True))



        print(list_of_urls)

        tupples = query_solr(search_text, Depth, list_of_strategy, list_of_urls)

        
     
        # for r in tupples[0]:
        #     print(r.text + " " + r.url + " " + str(r.depth) + " " + r.data_type)

        print(tupples)

        show_search=[]

        for r in tupples[0]:
            print(r.text + " " + r.page_url + " " + str(r.depth) + " " + r.data_type)

            result_text = r.text

            find_text = result_text.find(search_text)

            send_text = result_text[max(0,find_text-100):200]
            
            show_search.append(((send_text), ( r.page_url)))


        # return render(request, 'index.html', {'msg':show_search})

        return render(request, 'index.html', {'msg' : dict(show_search)})

