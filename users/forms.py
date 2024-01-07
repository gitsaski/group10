from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company, Employer, Employee, Profile

class EmployerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)
    contact_number = forms.CharField(required=True)
    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label=None, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "full_name", "contact_number", "company"]

class EmployeeRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "full_name", "phone_number"]

class CompanyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    company_name = forms.CharField(required=True)
    contact_number = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "company_name", "contact_number", "address"]

class CompanyUserRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 5}),
        }