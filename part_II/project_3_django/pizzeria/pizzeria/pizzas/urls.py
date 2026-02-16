from django.urls import path
from . import views


appname = "pizzas"


urlpatterns = [
    path("", views.index, name="index"),
]
