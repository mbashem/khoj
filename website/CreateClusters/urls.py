

from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='index'),
    path('StoreData', views.StoreData, name = 'storedata'),

]

