from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path("home", views.home, name="home"),
    path("add_todo/", views.add_todo),
    path("delete_todo/<int:todo_id>/", views.delete_todo),
]
