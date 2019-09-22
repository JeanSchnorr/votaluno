from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('AvaliacoesTurmas/', views.avaliacoesTurmas, name='avaliacoesTurmas'),
]
