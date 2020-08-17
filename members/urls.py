from django.urls import path
from members.views import UserRegisterView


urlpatterns = [
    path('cadastro/', UserRegisterView.as_view(), name='register'),
]
