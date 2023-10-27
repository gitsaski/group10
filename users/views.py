from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmployerRegistrationForm, EmployeeRegistrationForm


def registration(request):
    return render(request, 'registration/registration.html')

def registration_success_employee(request):
    return render(request, 'users/registration_success_employee.html')

def registration_success_employer(request):
    return render(request, 'users/registration_success_employer.html')


def employer_registration(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:registration_success_employer')
    else:
        form = EmployerRegistrationForm()

    return render(request, 'users/employer_registration.html', {'form': form})


def employee_registration(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:registration_success_employee')
    else:
        form = EmployeeRegistrationForm()

    return render(request, 'users/employee_registration.html', {'form': form})