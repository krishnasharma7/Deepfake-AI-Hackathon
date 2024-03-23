
from django.urls import path, include
from . import views

app_name = 'deepfake'
urlpatterns = [
    path("home/", views.home, name="home"),
    path("history/", views.history, name="history"),
]
