from django.shortcuts import render, get_object_or_404
from .models import HomePage, Department, Specialty, Teacher

def home(request):
    content = HomePage.objects.first()
    return render(request, 'core/home.html', {'content': content})

def program_list(request):
    specialties = Specialty.objects.select_related('department').all()
    return render(request, 'core/program_list.html', {'specialties': specialties})

def program_detail(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)
    return render(request, 'core/program_detail.html', {'specialty': specialty})

def department_list(request):
    departments = Department.objects.prefetch_related('specialties').all()
    return render(request, 'core/department_list.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    teachers = department.teachers.all()
    specialties = department.specialties.all()
    return render(request, 'core/department_detail.html', {
        'department': department,
        'teachers': teachers,
        'specialties': specialties,
    })