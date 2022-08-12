from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.db.models import Q
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from backend.apps.accounts.models import User
from backend.apps.school.forms import StudentCreateForm, StudentUpdateForm, StudentMailingForm
from backend.apps.school.models import Student, Mailing
from backend.apps.school.signals import student_created


class IndexView(generic.ListView):
    template_name = "index.html"
    model = Student
    context_object_name = 'students'

    def get_queryset(self):
        query_params = self.request.GET
        search_word = query_params.get('search_word')
        if search_word:
            students = Student.objects.filter(first_name__icontains=search_word) | \
                         Student.objects.filter(last_name__icontains=search_word) | \
                         Student.objects.filter(middle_name__icontains=search_word)
        else:
            students = Student.objects.all()
        return students


class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentCreateForm
    template_name = 'student_create.html'
    success_url = reverse_lazy('index')


class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentUpdateForm
    template_name = 'student_update.html'
    success_url = reverse_lazy('index')


class StudentListView(generic.ListView):
    template_name = "student_list.html"
    model = Student
    context_object_name = 'students'

    def get_queryset(self):
        query_params = self.request.GET
        search_word = query_params.get('search_word')
        if search_word:
            students = Student.objects.filter(first_name__icontains=search_word) | \
                       Student.objects.filter(last_name__icontains=search_word) | \
                       Student.objects.filter(middle_name__icontains=search_word)
        else:
            students = Student.objects.all()
        return students


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'


class StudentDeleteView(generic.DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = '/students/'


class StudentMailingView(generic.CreateView):
    model = Mailing
    form_class = StudentMailingForm
    template_name = "student_mailing.html"
    success_url = reverse_lazy('student_list')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            student_form = StudentMailingForm(request.POST)
            if student_form.is_valid():
                student_mails = student_form.save(commit=False)
                print(student_mails)
                students = student_form.cleaned_data['students']
                for student in students:
                    send_mail(student_form.cleaned_data['title'],
                              student_form.cleaned_data['text'],
                              settings.EMAIL_HOST_USER,
                              [student.email],
                              fail_silently=True,)
                student_mails = student_form.save()
            return render(request, 'mailing_done.html', {'student_mails': student_form})
        return HttpResponse(content=f'Похоже вы неправильно заполнили форму:')
