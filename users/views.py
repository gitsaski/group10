from django.shortcuts import render
from .forms import EmployerRegistrationForm
from .models import Employer

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
            return render(request, 'registration_success.html')  # Replace 'registration_success.html' with your desired success page
    else:
        form = EmployerRegistrationForm()
    return render(request, 'employer_registration.html', {'form': form})
