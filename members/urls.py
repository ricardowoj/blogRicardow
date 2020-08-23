from django.urls import path
from members.views import UserRegisterView, UserEditView


urlpatterns = [
    path('cadastro/', UserRegisterView.as_view(), name='register'),
    path('editar-cadastro/', UserEditView.as_view(), name='edit-profile'),
]
