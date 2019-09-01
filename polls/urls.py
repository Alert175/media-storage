from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.index),
    path("user=<str:user_name>", views.user_name),
    re_path(r"^user=$", views.user_name),
    re_path(r"^user$", views.user)
]