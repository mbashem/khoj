from django.urls import path
from django.views.generic import TemplateView
<<<<<<< HEAD

from . import views
from django.urls import path,include
=======
from . import views
from django.urls import path,include
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
>>>>>>> Maisha
urlpatterns = [

    path('', views.index),

]
<<<<<<< HEAD
=======
# urlpatterns += staticfiles_urlpatterns()

>>>>>>> Maisha
