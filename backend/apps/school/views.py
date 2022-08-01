from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from backend.apps.school.forms import StudentCreateForm, StudentUpdateForm
from backend.apps.school.models import Student


class IndexView(generic.TemplateView):
    template_name = "index.html"


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


def student_search(request):
    try:
        q = request.GET['q']
        students = Student.objects.filter(title__search=q) | \
                Student.objects.filter(intro__search=q) | \
                Student.objects.filter(content__search=q)
        return render('search/results.html', {'students':students, 'q':q})
    except KeyError:
        return render('search/results.html')


# def send_mail_task(user_email: str):
#     try:
#         send_mail(
#             'Вам пришло новое сообщение',
#             'Спасибо за оставленный комментарий',
#             settings.EMAIL_HOST_USER,  # отправитель
#             [user_email],  # получатели
#             fail_silently=True,
#         )
#     except Exception as exc:
#         print(f'Occurred error {exc}')


