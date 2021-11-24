from django.urls import path
from django.views.generic import TemplateView


from . import views
from django.urls import path,include

from . import views
from django.urls import path,include
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [

    path('', views.index),

]

