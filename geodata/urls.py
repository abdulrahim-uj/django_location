from django.urls import path
from . import views

app_name = "geodata"

urlpatterns = [
    path('', views.index, name='home'),
]