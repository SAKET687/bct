from django.contrib import admin  # type: ignore
from django.urls import path, include  # type:ignore

urlpatterns = [path("", include("app.urls"))]
