from django.urls import path

from . import views

app_name = 'training'
urlpatterns = [
    path("", views.trainingindex, name="trainingindex"),
    path('create/', views.create, name='create'),
    path('appliance/', views.appliance, name='appliance')
]