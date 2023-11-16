from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EmployerRegistrationForm, EmployeeRegistrationForm, CompanyRegistrationForm, CompanyUserRegistrationForm
from .models import Company  # Import the Company model

def registration(request):
    return render(request, 'registration/registration.html')

def registration_success_employee(request):
    return render(request, 'users/registration_success_employee.html')

def registration_success_employer(request):
    return render(request, 'users/registration_success_employer.html')

def registration_success_company(request):
    return render(request, 'users/registration_success_company.html')

def employer_registration(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            company = form.cleaned_data['company']
            Company.objects.create(user=user, company_name=company.company_name, contact_number=company.contact_number, address=company.address)

            login(request, user)
            messages.success(request, 'Employer registration successful.')
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
            messages.success(request, 'Employee registration successful.')
            return redirect('users:registration_success_employee')
    else:
        form = EmployeeRegistrationForm()

    return render(request, 'users/employee_registration.html', {'form': form})

@login_required
def company_registration(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to create a company.')
        return redirect('some_redirect_url')  # Redirect to a suitable URL for non-admin users

    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Company registration successful.')
            return redirect('users:registration_success_company')
    else:
        form = CompanyRegistrationForm()

    return render(request, 'users/company_registration.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
