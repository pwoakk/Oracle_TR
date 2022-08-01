from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from backend.apps.accounts.models import TeacherProfile, User


class TeacherProfileInline(admin.StackedInline):
    model = TeacherProfile
    can_delete = False
    verbose_name_plural = "Учителя"
    fk_name = "user"


@admin.register(User)
class AllUserAdmin(UserAdmin):
    inlines = [TeacherProfileInline]
    list_display = [
        'phone',
        'first_name',
        'middle_name',
        'last_name',
        'is_active',
    ]

    add_fieldsets = (
        (None, {'fields': ('phone', 'first_name', 'middle_name',  'last_name', 'is_active', 'password1', 'password2'), }),
    )
    fieldsets = (
        (None, {'fields': ('phone', 'first_name', 'middle_name',  'last_name', 'is_active', 'password'), }),
    )
    ordering = ['-id']
