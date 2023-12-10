from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EmployerRegistrationForm, EmployeeRegistrationForm, CompanyRegistrationForm
from .models import Employer, Employee, Company, Profile

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
            employer = Employer.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                contact_number=form.cleaned_data['contact_number'],
                company=company,
            )
            # create or update the user's profile
            profile, created = Profile.objects.get_or_create(user=user)
            profile.employer = employer
            profile.save()

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

            # create and associate the employee instance with the user's profile
            employee = Employee.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
            )
            # create or update the user's profile
            profile, created = Profile.objects.get_or_create(user=user)
            profile.employee = employee
            profile.save()

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
            Company.objects.create(
                user=user,
                name=form.cleaned_data['company_name'],
                contact_number=form.cleaned_data['contact_number'],
                address=form.cleaned_data['address'],
            )

            login(request, user)
            messages.success(request, 'Company registration successful.')
            return redirect('users:registration_success_company')
    else:
        form = CompanyRegistrationForm()

    return render(request, 'users/company_registration.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def edit_profile(request):
    return render(request, 'users/edit_profile.html')
