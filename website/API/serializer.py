from rest_framework import serializers

from auth_app.models import *
from CreateClusters.models import *

from rest_framework.exceptions import AuthenticationFailed
import os



class ClustersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clusters
        fields = ['cluster_id','user_name', 'cluster_name', 'depth', 'isScrapedCluster']
        # lookup_filed = 'cluster_id'

class AuthUserSerializer(serializers.ModelSerializer):
    user_has_clusters = ClustersSerializer(many=True, read_only=True)
    class Meta:
        model = AuthUser
        fields = ['username', 'user_has_clusters']




