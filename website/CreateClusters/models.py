from django.db import models
from auth_app.models import AuthUser, AuthGroup, AuthPermission, AccountEmailaddress, AuthUserGroups, AuthUserUserPermissions, AccountEmailconfirmation, AuthGroupPermissions, DjangoAdminLog, AccountEmailaddress, DjangoSite, DjangoSession, DjangoMigrations, DjangoContentType, SocialaccountSocialappSites, SocialaccountSocialtoken, SocialaccountSocialaccount, SocialaccountSocialapp
# Create your models here.

class Clusters(models.Model):
    cluster_id = models.AutoField(db_column='Cluster_ID', primary_key=True)  # Field name made lowercase.
    user_name = models.ForeignKey('auth_app.AuthUser', models.DO_NOTHING, db_column='User_Name')  # Field name made lowercase.
    cluster_name = models.TextField(db_column='Cluster_Name', unique=True)  # Field name made lowercase.
    depth = models.SmallIntegerField(db_column='Depth')  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'Clusters'
        unique_together = ('cluster_id', 'cluster_name')

    def __str__(self):
        return self.cluster_name


class CrawlingStrategy(models.Model):
    strategy_name = models.TextField(db_column='Strategy_Name', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Crawling_Strategy'

    def __str__(self):
        return self.strategy_name


class UrlList(models.Model):
    url_id = models.BigAutoField(db_column='URL_ID', primary_key=True)  # Field name made lowercase.
    cluster = models.ForeignKey(Clusters, models.DO_NOTHING, db_column='Cluster_ID')  # Field name made lowercase.
    url_name = models.TextField(db_column='URL_Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'URL_List'

    def __str__(self):
        return self.url_name


class ClusterStrategy(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cluster = models.ForeignKey('Clusters', models.DO_NOTHING, db_column='Cluster_ID')  # Field name made lowercase.
    strategy = models.ForeignKey('CrawlingStrategy', models.DO_NOTHING, db_column='Strategy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cluster_Strategy'

    def __str__(self):
        return self.strategy
