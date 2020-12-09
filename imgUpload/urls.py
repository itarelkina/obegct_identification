from django.conf.urls import url, include
from django.urls import path
from . import views
urlpatterns = [
    url('imageprocess', views.imageProcess, name='imageprocess'),
    url(r'^$',views.home, name='home'),
    #path('', views.home, name='home')
]