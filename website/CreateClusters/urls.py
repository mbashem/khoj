from django.urls import path
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.urls import path,include
urlpatterns = [

    path('', views.index),

]
urlpatterns += staticfiles_urlpatterns()

