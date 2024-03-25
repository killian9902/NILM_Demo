from django.urls import path

from . import views

app_name = 'testing'
urlpatterns = [
    path("", views.testingindex, name="testingindex"),
    path("AI/", views.AI, name="AI")
]