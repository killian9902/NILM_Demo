from django.urls import path

from . import views

app_name = 'explain'
urlpatterns = [
    path("", views.explainindex, name="explainindex")
]