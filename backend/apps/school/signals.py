from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from backend.apps.school.models import Student
from backend.config import settings


@receiver(post_save, sender=Student)
def student_created(sender, instance, created, **kwargs):
    if created:
        firstname = instance.first_name
        email = instance.email
        print(email)
        send_mail(firstname, 'Ваш профиль добавлен', settings.EMAIL_HOST_USER,
                  [email], fail_silently=False)
