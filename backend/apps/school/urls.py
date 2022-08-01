from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    ]