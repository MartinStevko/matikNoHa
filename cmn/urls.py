from django.urls import path

from . import views

app_name = 'cmn'

urlpatterns = [
    path('posts', views.posts),
    path('posts/new', views.new),
    path('manager', views.manager),
    path('approve/<int:url>', views.approve),
    path('', views.index),
]
