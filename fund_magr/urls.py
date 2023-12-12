from django.urls import path
from fund_magr import views

urlpatterns = [
    path('home', views.home),
    path('viewport', views.viewport),
    path('seechart', views.seechart)
]

