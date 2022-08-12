from django.forms import ModelForm
from django import forms

from backend.apps.school.models import Student, Mailing


class StudentCreateForm(ModelForm):

    first_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'})
    )
    middle_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'})
    )
    last_name = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'})
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
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Класс'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Пол'}),
        }


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'address',
            'email',
            'grade',
        ]
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'grade': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Класс'}),
        }


class StudentMailingForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(),)
                                               # widget=forms.CheckboxSelectMultiple(attrs={'placeholder': 'Исполнитель'}))

    class Meta:
        model = Mailing
        fields = [
            'title',
            'text',
            'students',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }
