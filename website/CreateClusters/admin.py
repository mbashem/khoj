from django.contrib import admin
# Register your models here.
from .models import Clusters, CrawlingStrategy, UrlStrategy, UrlList

admin.site.register(Clusters)
admin.site.register(CrawlingStrategy)
admin.site.register(UrlList)
admin.site.register(UrlStrategy)