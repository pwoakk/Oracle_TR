from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from backend.apps.accounts.forms import UserUpdateForm, UserRegisterForm, LoginForm
from backend.apps.accounts.models import User, TeacherProfile


class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        phone = data['phone']
        password = data['password']
        user = authenticate(phone=phone, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponse('Ваш аккаунт неактивен')
        return HttpResponse('Такого пользователя не существует')


class UserRegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')


class RegisterDoneView(generic.TemplateView):
    template_name = 'register_done.html'


class UserProfileView(LoginRequiredMixin, generic.ListView):
    model = TeacherProfile
    template_name = 'profile.html'
    context_object_name = 'about'

    # def get_queryset(self):
    #     queryset = Task.objects.filter(author=self.request.user)
    #     return queryset

    @staticmethod
    def post_authors():
        return User.objects.filter(role=False)


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        if self.kwargs.get('pk') == self.request.user.pk:
            return True
        return False


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('logout')