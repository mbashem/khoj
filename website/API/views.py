from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from CreateClusters.models import Clusters
from .serializer import *


@api_view(['GET'])
def get_cluster(request):
    if request.method == 'GET':
        user_name = request.data.get('user_name')

        if user_name is not None:
            print(user_name)
            clusters_list = Clusters.objects.filter(user_name=user_name).values_list('cluster_name', 'depth', 'isScrapedCluster')
            print(clusters_list)
            return Response(clusters_list)






