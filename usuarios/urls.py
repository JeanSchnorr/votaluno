from django.urls import path ,include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('sair/', auth_views.LogoutView.as_view(template_name='login.html'), name='sair'),
    path('entrar/', auth_views.LoginView.as_view(template_name='login.html'), name='entrar'),
] 