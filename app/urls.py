from django.urls import path  # type:ignore
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("home/", views.home_view, name="home"),
]
