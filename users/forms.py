from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)
    contact_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "full_name", "contact_number"]


class EmployeeRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)
    contact_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "full_name", "contact_number"]
