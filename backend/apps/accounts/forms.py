from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.core import validators

from backend.apps.accounts.models import User


class LoginForm(forms.Form):
    phone = forms.CharField(
        validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(10)],
        label='Телефон',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ТЕЛЕФОН'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'autocomplete': 'off',
            'placeholder': 'Пароль'
        })
    )


class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(
        validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(10)],
        label='Телефон',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'})
    )
    first_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'})
    )
    middle_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'})
    )
    last_name = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'})
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль повторно'})
    )

    class Meta:
        model = User
        fields = [
            'phone',
            'first_name',
            'middle_name',
            'last_name',
        ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'phone',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
