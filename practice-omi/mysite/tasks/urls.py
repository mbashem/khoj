from django.urls import path, include
from .import views

urlpatterns = [

    path('', views.index),
    path('profile', views.profile),
    path('file', views.file),
    path('checkcommand', views.Check_Command),


]