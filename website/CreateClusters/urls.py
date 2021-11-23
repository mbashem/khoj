from django.urls import path
from django.views.generic import TemplateView
<<<<<<< HEAD
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
=======

>>>>>>> omi
from . import views
from django.urls import path,include
urlpatterns = [

    path('', views.index),

]
<<<<<<< HEAD
urlpatterns += staticfiles_urlpatterns()

=======
>>>>>>> omi
