from django.contrib import admin

from backend.apps.school.models import School, Grade, Subject, Student


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

