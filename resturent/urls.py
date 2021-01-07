# urls.py
from django.urls import path

from . import views

urlpatterns = [
path("", views.ResturentSearchList.as_view())
]