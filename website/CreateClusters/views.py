import os

from django.shortcuts import render, redirect
from django.db import connection, connections

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

    ClusterName = request.POST.get("ClusterName")
    Depth = int(request.POST.get("DEPTH"))
    PDF = request.POST.get("PDF")
    TXT = request.POST.get("TXT")
    DOCX = request.POST.get("DOCX")
    XML = request.POST.get("XML")
    ALLTEXT = request.POST.get("ALLTEXT")
    URLS = request.POST.getlist("URLS")
    UserName = request.POST.get("username")



    cursor = connection.cursor()

    row = cursor.execute("""select * from "Clusters" where "User_Name"= %s and "Cluster_Name" = %s""", (UserName, ClusterName))
    cnt = cursor.rowcount

    # inserting cluster name in db/ prevents adding if the name already exists for a same user
    if cnt == 0:
        cursor.execute("""INSERT INTO "Clusters"("User_Name", "Cluster_Name", "Depth") VALUES (%s, %s, %s)""", (UserName, ClusterName, Depth))
    else:
        params = {'msg' : 'Cluster Name already exist. Give another name!'}
        return render(request, 'CreateClusters/ClusterIndex.html', params)

    # inserting urls in db
    for url in URLS:
        cursor.execute("""INSERT INTO "URL_List"("Cluster_ID", "URL_Name")
            VALUES ((select "Cluster_ID" from "Clusters" where "Cluster_Name"=%s), %s);""", (ClusterName, url))


    #for .pdf
    if PDF == "on":
        cursor.execute("""INSERT INTO "Cluster_Strategy"("Cluster_ID", "Strategy")
        VALUES ((select "Cluster_ID" from "Clusters" where "Cluster_Name"=%s), '.pdf')""", [ClusterName])

    # for .txt
    if TXT == "on":
        cursor.execute("""INSERT INTO "Cluster_Strategy"("Cluster_ID", "Strategy")
        VALUES ((select "Cluster_ID" from "Clusters" where "Cluster_Name"=%s), '.txt')""", [ClusterName])

    # for .docx
    if DOCX == "on":
        cursor.execute("""INSERT INTO "Cluster_Strategy"("Cluster_ID", "Strategy")
        VALUES ((select "Cluster_ID" from "Clusters" where "Cluster_Name"=%s), '.docx')""", [ClusterName])

    # for .xml
    if XML == "on":
        cursor.execute("""INSERT INTO "Cluster_Strategy"("Cluster_ID", "Strategy")
        VALUES ((select "Cluster_ID" from "Clusters" where "Cluster_Name"=%s), '.xml')""", [ClusterName])

    # for all text
    if ALLTEXT == "on":
        cursor.execute("""INSERT INTO "Cluster_Strategy"("Cluster_ID", "Strategy")
        VALUES ((select "Cluster_ID" from "Clusters" where "Cluster_Name"=%s), 'all text')""", [ClusterName])


    begin_crawl(URLS = URLS,height = Depth)



    return render(request, 'CreateClusters/ClusterIndex.html', {'msg' : 'cluster created successfully. System will let you know when it is ready to search'})



