
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('yielp', views.yielpCapture, name="yielp"),

    
    path('',include("food.modules.company.urls")),
]
