
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from project_root.views import *
from .serializer import *
import json
import requests




#this api method privodes the search results of a text as a dictionary
@api_view()
@permission_classes([AllowAny])
def search_result_api(request):

    # print(request.query_params)

    user_name = request.query_params['user_name']
    depth = request.query_params.getlist('depth')
    search_text = request.query_params['searchtext']
    clusters = request.query_params.getlist('clusters')

    # print(user_name)
    # print(depth)
    # print(search_text)
    # print(clusters)

    api_result = find_text(user_name, clusters, depth, search_text)


    return Response({'msg': dict(api_result)})





class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuthUser.objects.filter(username='farhan_ishraq_omi')
    serializer_class = AuthUserSerializer



# api viewset for showing all the clusters of a user
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




@api_view()
@permission_classes([AllowAny])
def verify_user(request):

    id_token = request.query_params['id_token']
    try:

        URL = 'https://oauth2.googleapis.com/tokeninfo?id_token=' + id_token

        headers = {'content-Type': 'application/json'}

        r = requests.get(url=URL, headers=headers)
        data = r.json()

        print(data)

        user_email = data['email']

        print(user_email)

        is_user_exists = AuthUser.objects.filter(email=user_email).first()

        if is_user_exists is not None:

            user_name = is_user_exists.username
            print(user_name)
            values = {'status': "OK", "username": user_name}
            return Response({'status' : 'OK', 'username' : user_name})

        return Response({'status':'Failed!'})

    except:

        return Response({'status': 'FAILED'})



























