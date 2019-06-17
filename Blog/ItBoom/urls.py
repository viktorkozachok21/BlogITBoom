# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sendoffer/', views.sendoffer, name="sendoffer"),
    path('sendmessage/', views.sendmessage, name="sendmessage"),
    path('showarticle/', views.showarticle, name="showarticle"),
    path('shownews/', views.shownews, name="shownews"),
]
