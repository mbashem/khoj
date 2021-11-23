from django.urls import path
from django.views.generic import TemplateView

from . import views
from django.urls import path,include
urlpatterns = [

    path('', views.index),

]
