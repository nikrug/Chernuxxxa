from _operator import index

from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
  path('', views.rick),
  path('/rick',views.rick)
    ]