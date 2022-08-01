from django.forms import ModelForm
from django import forms

from backend.apps.school.models import Student


class StudentCreationForm(ModelForm):

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

    class Meta:
        model = Student
        fields =[
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'birthdate',
            'grade',
            'address',
            'gender',
        ]
