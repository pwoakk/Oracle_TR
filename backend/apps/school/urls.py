from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('student/create/', StudentCreateView.as_view(), name='student_create'),
    path('student/update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('students/', StudentListView.as_view(), name='student_list'),
    ]