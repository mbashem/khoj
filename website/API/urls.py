from django.contrib import admin

from django.urls import path, include
from API import views
from rest_framework.routers import DefaultRouter

from API.views import ClusterViewSet, search_result_api

router = DefaultRouter()

router.register('cluster_get', views.ClusterViewSet, basename='cluster_get')
router.register('user_get', views.UserViewSet, basename='user_get')
# router.register('searchtext', views.search_result_api, basename='searchtext')



urlpatterns = [
    path('', include(router.urls)),
    path('searchtext/', search_result_api),


]

