"""define Url patterns for learning_logs"""

from django.urls import path

from . import views


appname = "learning_logs"
urlpatterns = [
    # Home page
    path("", views.index, name="index")
]
