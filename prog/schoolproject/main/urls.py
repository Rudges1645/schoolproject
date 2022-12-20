from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('lazy', views.lazy),
    path('about', views.about),
    path('products', views.products),
    path('connect', views.connect),
    path('support', views.support),
]