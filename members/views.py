from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, LoginView
from members.forms import SignUpForm, EditProfileForm, PasswordChangingForm, LoginForm


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = './registration/login.html'
    sucess_url = reverse_lazy('home')


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = './registration/change-password.html'
    success_url = reverse_lazy('home')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = './registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = './registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
