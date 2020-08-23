from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', UserRegisterView.as_view(), name='register'),
    path('editar-cadastro/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(), name='edit-password'),
]
