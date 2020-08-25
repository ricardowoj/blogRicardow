from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, UserLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('cadastro/', UserRegisterView.as_view(), name='register'),
    path('editar-cadastro/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(), name='edit-password'),
]
