from django.shortcuts import render
from django.contrib.auth import login
from .forms import EmployerRegistrationForm, EmployeeRegistrationForm
from .models import Employer, Employee


def registration(request):
    return render(request, 'registration/registration.html')


def employer_registration(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            # Create an instance of Employer and save it to the database
            employer = Employer(
                full_name=form.cleaned_data['full_name'],
                company_name=form.cleaned_data['company_name'],
                email=form.cleaned_data['email'],
                contact_number=form.cleaned_data['contact_number'],
                company_location=form.cleaned_data['company_location'],
                industry=form.cleaned_data['industry'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                company_description=form.cleaned_data['company_description']
            )
            employer.save()
            return render(request, 'registration_success_employer.html') 
    else:
        form = EmployerRegistrationForm()
    return render(request, 'employer_registration.html', {'form': form})


def employee_registration(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            # Create an instance of Employee and save it to the database
            employee = Employee(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                contact_number=form.cleaned_data['contact_number'],
                address=form.cleaned_data['address'],
                job_title=form.cleaned_data['job_title'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            employee.save()
            return render(request, 'registration_success_employee.html') 
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'employee_registration.html', {'form': form})