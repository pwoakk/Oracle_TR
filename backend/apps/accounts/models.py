from django.contrib.auth.models import AbstractUser
from django.db import models

from backend.apps.accounts.managers import UserManager
from backend.apps.school.models import Grade, Subject


class User(AbstractUser):
    username = None
    phone = models.CharField('Номер телефона', max_length=10, unique=True)
    first_name = models.CharField('Фамилия', max_length=50, blank=True)
    middle_name = models.CharField('Имя', max_length=50, blank=True)
    last_name = models.CharField('Отчество', max_length=50, blank=True)
    is_active = models.BooleanField('Статус', default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='teacher',
        verbose_name='Преподаватель',
    )
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name='teachers')

    class Meta:
        verbose_name = 'Профиль преподавателя'
        verbose_name_plural = 'Профили преподавателей'

    def __str__(self):
        return f'{self.user.first_name}'

