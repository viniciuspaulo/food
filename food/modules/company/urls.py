
from django.contrib import admin
from django.urls import path, include
from . import views

module = "admin/food/company"

urlpatterns = [
    path(module+"/", views.index, name="company_list"),
    path(module+"/new", views.store, name="company_new"),
    path(module+"/edit/<int:pk>", views.update, name="company_edit"),
    path(module+"/delete/<int:pk>", views.delete, name="company_delete"),
]
