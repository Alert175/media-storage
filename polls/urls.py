from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.index),
    # re_path(r"^user=(?P<user_name>\w+)", views.user_name, name="user_name"),
    path("user=<str:user_name>", views.user_name),
    re_path(r"^user=$", views.user_name),
    re_path(r"^user$", views.user)
]