from django.contrib import admin

from django.conf.urls import url

from django.urls import path, include
from API import views
from rest_framework.routers import DefaultRouter

from API.views import ClusterViewSet, search_result_api, verify_user

router = DefaultRouter()

router.register('cluster_get', views.ClusterViewSet, basename='cluster_get')
router.register('user_get', views.UserViewSet, basename='user_get')



urlpatterns = [
    path('', include(router.urls)),
    url('searchtext/', search_result_api),
    url('verify_user/', verify_user),



]

