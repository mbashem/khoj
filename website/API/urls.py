from django.urls import path

from django.urls import path
from API import views

urlpatterns = [
    path('get_cluster/', views.get_cluster),

]

