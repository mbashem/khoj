from django.contrib import admin
# Register your models here.
from .models import Clusters, CrawlingStrategy, ClusterStrategy, UrlList

admin.site.register(Clusters)
admin.site.register(CrawlingStrategy)
admin.site.register(UrlList)
admin.site.register(ClusterStrategy)