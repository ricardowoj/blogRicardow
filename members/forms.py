from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        label="Usuário",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100,
        label="Nome",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100,
        label="Sobrenome",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        max_length=100,
        label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        max_length=100,
        label="Confirmar senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')


class EditProfileForm(UserChangeForm):
    UserChangeForm.password = None
    username = forms.CharField(
        max_length=100,
        label="Usuário",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100,
        label="Nome",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100,
        label="Sobrenome",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=100,
        label="Senha atual",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password'
        }))
    new_password1 = forms.CharField(
        max_length=100,
        label="Nova senha",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password'
        }))
    new_password2 = forms.CharField(
        max_length=100,
        label="Confirme a senha",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password'
        }))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')