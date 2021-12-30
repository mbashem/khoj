
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from snippets import views

router = DefaultRouter()

router.register('studentapi', views.StudentModelView, basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api', views.student_api),
    # path('', include(router.urls))
    path('stuinfo/<int:pk>', views.student_detail),
    # path('stuinfo/', views.StudentCreate.as_view()),
    # path('stucreate/', views.student_create),
    path('stuapi/', views.student_api),
    url('searchtext/', views.search_result_api)
]
