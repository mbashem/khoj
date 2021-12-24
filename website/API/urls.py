from django.contrib import admin

from django.urls import path, include
from API import views
from rest_framework.routers import DefaultRouter

from API.views import ClusterViewSet

router = DefaultRouter()

router.register('cluster_get', views.ClusterViewSet, basename='cluster_get')
router.register('user_get', views.UserViewSet, basename='user_get')



urlpatterns = [
    path('', include(router.urls)),


]

