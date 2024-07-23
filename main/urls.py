from django.urls import path

from . import views

urlpatterns = [
path("<int:id>",views.index , name = "index"),
path("",views.home , name = "home"),
path("home/",views.home , name = "home"),
path("create/",views.create , name = "create"),
path("delete/",views.delete , name = "delete"),
path("edit/<int:id>",views.edit , name = "edit"),
]