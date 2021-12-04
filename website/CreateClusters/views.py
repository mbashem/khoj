import os

from django.shortcuts import render, redirect
from django.db import connection, connections

from django.core.exceptions import ObjectDoesNotExist

from CreateClusters.spiders import begin_crawl


from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
# Create your views here.

from django.http import  HttpResponse

from CreateClusters.models import *


def index(request):
    return render(request, 'CreateClusters/ClusterIndex.html')





# this method stores cluster information in database
def StoreData(request):

    #received value through html form
    ClusterName = request.POST.get("ClusterName")
    Depth = int(request.POST.get("DEPTH"))
    PDF = request.POST.get("PDF")
    TXT = request.POST.get("TXT")
    DOCX = request.POST.get("DOCX")
    XML = request.POST.get("XML")
    ALLTEXT = request.POST.get("ALLTEXT")
    URLS = request.POST.getlist("URLS")
    UserName = request.POST.get("username")

    #checking if a cluster exists of the user with the same name given in the form
    try:
        isClusterExist = Clusters.objects.get(user_name=UserName, cluster_name=ClusterName)

        params = {'msg': 'Cluster Name already exist. Give another name!'}
        #returns a message if a cluster exists with the same name of a user
        return render(request, 'CreateClusters/ClusterIndex.html', params)

    # insert cluster name and depth
    except ObjectDoesNotExist:
        auth_user_object = AuthUser.objects.get(username=UserName)
        create_this_cluster = Clusters(user_name=auth_user_object, cluster_name=ClusterName, depth=Depth)
        create_this_cluster.save()

    Cluster_object = Clusters.objects.get(user_name=UserName, cluster_name=ClusterName)


    #inserting urls of a cluster
    for url in URLS:

        insert_url = UrlList(cluster=Cluster_object, url_name=url)

        insert_url.save()

    #for .pdf
    if PDF == "on":
        strategy_object_pdf = CrawlingStrategy.objects.get(strategy_name='.pdf')
        save_strategy_pdf = ClusterStrategy(cluster=Cluster_object, strategy=strategy_object_pdf)
        save_strategy_pdf.save()

    # for .txt
    if TXT == "on":
        strategy_object_txt = CrawlingStrategy.objects.get(strategy_name='.txt')
        save_strategy_txt = ClusterStrategy(cluster=Cluster_object, strategy=strategy_object_txt)
        save_strategy_txt.save()

    # for .docx
    if DOCX == "on":
        strategy_object_docx = CrawlingStrategy.objects.get(strategy_name='.docx')
        save_strategy_docx = ClusterStrategy(cluster=Cluster_object, strategy=strategy_object_docx)
        save_strategy_docx.save()

    # for .xml
    if XML == "on":
        strategy_object_xml = CrawlingStrategy.objects.get(strategy_name='.xml')
        save_strategy_xml = ClusterStrategy(cluster=Cluster_object, strategy=strategy_object_xml)
        save_strategy_xml.save()

    # for all text
    if ALLTEXT == "on":
        strategy_object_all_text = CrawlingStrategy.objects.get(strategy_name='all text')
        save_strategy_all_text = ClusterStrategy(cluster=Cluster_object, strategy=strategy_object_all_text)
        save_strategy_all_text.save()


    begin_crawl(URLS, Depth)


    return render(request, 'CreateClusters/ClusterIndex.html', {'msg' : 'cluster created successfully. System will let you know when it is ready to search'})

