from django.urls import path

from . import views

app_name = 'homepage'
urlpatterns = [
    path("", views.homeindex, name="homeindex"),
]