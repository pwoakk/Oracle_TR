from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *


urlpatterns = [
    path('profile/teacher/', UserProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', user_logout, name='logout'),
    path('user/profile/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/change-password/', UserPasswordChangeView.as_view(), name='change_password')
]