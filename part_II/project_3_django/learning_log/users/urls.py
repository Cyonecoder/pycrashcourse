from django.urls import path, include

app_name = "users"

urlpaterns = [path("", include("django.contrib.auth.urls"))]
