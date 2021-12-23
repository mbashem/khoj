from rest_framework import serializers

from auth_app.models import *
from CreateClusters.models import *


# class AuthUserSerializer(serializers.Serializer):
#     password = serializers.CharField(max_length=128)
#     last_login = serializers.DateTimeField(blank=True, null=True)
#     is_superuser = serializers.BooleanField()
#     username = serializers.CharField(unique=True, max_length=150, primary_key=True)
#     first_name = serializers.CharField(max_length=150)
#     last_name = serializers.CharField(max_length=150)
#     email = serializers.CharField(max_length=254)
#     is_staff = serializers.BooleanField()
#     is_active = serializers.BooleanField()
#     date_joined = serializers.DateTimeField()
#
#
#
# class ClustersSerializer(serializers.Serializer):
#     cluster_id = serializers.AutoField(db_column='Cluster_ID', primary_key=True)
#     user_name = serializers.ForeignKey('auth_app.AuthUser', models.DO_NOTHING, db_column='User_Name')
#     cluster_name = serializers.TextField(db_column='Cluster_Name', unique=True)
#     depth = serializers.SmallIntegerField(db_column='Depth')
#     isScrapedCluster = serializers.BooleanField(default=False)
#
#
#
# class CrawlingStrategySerializer(serializers.Serializer):
#     strategy_name = serializers.TextField(db_column='Strategy_Name', primary_key=True)  # Field name made lowercase.
#
#
#
# class UrlListSerializer(serializers.Serializer):
#     url_id = serializers.BigAutoField(db_column='URL_ID', primary_key=True)  # Field name made lowercase.
#     cluster = serializers.ForeignKey(Clusters, models.DO_NOTHING, db_column='Cluster_ID')  # Field name made lowercase.
#     url_name = serializers.TextField(db_column='URL_Name')
#
#
#
#
# class ClusterStrategySerializer(serializers.Serializer):
#     id = serializers.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     cluster = serializers.ForeignKey('Clusters', models.DO_NOTHING, db_column='Cluster_ID')  # Field name made lowercase.
#     strategy = serializers.ForeignKey('CrawlingStrategy', models.DO_NOTHING, db_column='Strategy')  # Field name made lowercase.






class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = "__all__"


class ClustersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clusters
        # fields = ['cluster_name', 'depth', 'isScrapedCluster']
        fields = "__all__"
        depth = 1

class CrawlingStrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawlingStrategy
        fields = "__all__"

class UrlListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlList
        fields = "__all__"

class ClusterStrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClusterStrategy
        fields = "__all__"

