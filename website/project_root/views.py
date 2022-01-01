import os

from django.shortcuts import render, redirect
from django.db import connection, connections

from django.core.exceptions import ObjectDoesNotExist

from auth_app import *

from django.http import HttpResponse
from CreateClusters.models import *
from auth_app.models import *
from indexer.query import *

from indexer.IndexResult import *

# this method shows all the clusters of a user in front page in template
def index(request):
    if request.user.is_authenticated:
        show_clusters_user = Clusters.objects.filter(user_name=request.user.username).values_list('cluster_name', 'depth', 'isScrapedCluster')

        params = {'Query': show_clusters_user, 'msg': 'here are your clusters!'}

        # print(show_clusters_user)
        # print(request.user.username)

        return render(request, 'index.html', params)

    else:

        params = {'msg': 'login to view clusters'}
        return render(request, 'index.html', params)


# query to get cluster_id of the selected clusters
def get_cluster_id(username, cluster_name):
    obj_of_cluster = Clusters.objects.get(user_name=username, cluster_name=cluster_name)
    cluster_id = obj_of_cluster.cluster_id
    return cluster_id


# query to get strategy list of the selected cluster
def get_list_of_strategy(cluster_id):
    list_of_strategy = list(ClusterStrategy.objects.filter(cluster=cluster_id).values_list('strategy', flat=True))
    return list_of_strategy


# query to get strategy list of urls of the selected cluster
def get_list_of_urls(cluster_id):
    list_of_urls = list(UrlList.objects.filter(cluster=cluster_id).values_list('url_name', flat=True))
    return list_of_urls


#this method supplies the search result of a text provided by the user as a tuple
def find_text(user_name, cluster_name, depth, search_text):

    show_search = []

    for (i, j) in zip(cluster_name, depth):

        print("for cluster ---> " + i)

        print("depth is ---> " + j)

        cluster_id = get_cluster_id(user_name, i)

        list_of_strategy = get_list_of_strategy(cluster_id)
        print("strategy list ---> ")
        print(list_of_strategy)


        list_of_urls = get_list_of_urls(cluster_id)
        print("url list ---> ")
        print(list_of_urls)

        tupples = query_solr(search_text, int(j), list_of_strategy, list_of_urls)
        print(tupples)

        for r in tupples[0]:
            print(r.text + " " + r.page_url + " " + str(r.depth) + " " + r.data_type)

            result_text = r.text

            find_text = result_text.find(search_text)

            send_text = result_text[max(0, find_text - 100):200]

            show_search.append(((send_text), (r.page_url)))

            # show_search.append(({'key':(send_text), 'url':(r.page_url)}))


    return show_search



# this method does the search in solr and returns the result as a dictionary
def search_result(request):
    # received value through html form
    search_text = request.POST.get("search_text")
    Depth = (request.POST.getlist("depth"))
    UserName = request.POST.get("user_name")
    Cluster_Name = request.POST.getlist("selected_cluster")

    print(search_text)
    print(Depth)
    print(UserName)
    print(Cluster_Name)

    show_search = find_text(UserName, Cluster_Name, Depth, search_text)

    return render(request, 'search.html', {'msg': dict(show_search)})
