
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import viewsets

from CreateClusters.models import Clusters
from .serializer import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.views import View




@api_view()
@permission_classes([AllowAny])
def search_result_api(request):
    print(request.query_params)
    return Response({'msg': 'here is the request'})





class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuthUser.objects.filter(username='farhan_ishraq_omi')
    serializer_class = AuthUserSerializer




class ClusterViewSet(viewsets.ViewSet):

     def list(self, request):
         clusters = Clusters.objects.all()
         serializers = ClustersSerializer(clusters, many=True)
         return Response(serializers.data)

     def retrieve(self, request, pk=None):
         id = pk
         if id is not None:
             clusters = Clusters.objects.filter(user_name = id)
             serializers = ClustersSerializer(clusters, many=True)
             return Response(serializers.data)






























#
# @api_view(['GET'])
# def get_cluster(request):
#     if request.method == 'GET':
#         user_name = request.data.get('user_name')
#
#         if user_name is not None:
#             print(user_name)
#             clusters_list = list(Clusters.objects.filter(user_name=user_name).values_list('cluster_name', 'depth', 'isScrapedCluster'))
#             serializers = ClustersSerializer(clusters_list, many=True)
#             print(serializers.data)
#             return Response(serializers.data)

#
# def get_cluster(self, request, *args, **kwargs):
#     json_data = request.body
#     stream = io.BytesIO(json_data)
#     python_data = JSONParser().parse(stream)
#
#     user_name = python_data.get('user_name', None)
#     print(user_name)
#
#     if user_name is not None:
#         clusters_list = Clusters.objects.filter(user_name=user_name).values_list('cluster_name', 'depth',
#                                                                                  'isScrapedCluster')
#         print(clusters_list)
#         serializers = ClustersSerializer(clusters_list, many=True)
#         json_data = JSONRenderer().render(serializers.data)
#         return HttpResponse(json_data, content_type='application/json')
