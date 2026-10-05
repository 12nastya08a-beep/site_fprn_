from django.contrib import admin
from .models import HomePage, Department, Specialty, Teacher

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head')
    search_fields = ('name', 'head')

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department', 'coordinator_name')
    list_filter = ('department',)
    search_fields = ('name', 'code')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'degree', 'department')
    list_filter = ('department',)
    search_fields = ('name', 'position')

from django.contrib import admin
from .models import ExchangeProgram

@admin.register(ExchangeProgram)
class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ('university_name', 'country', 'languages', 'slots', 'deadline')