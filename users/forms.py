from django import forms

class EmployerRegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Full Name')
    company_name = forms.CharField(max_length=100, label='Company Name')
    email = forms.EmailField(label='Email Address')
    contact_number = forms.CharField(max_length=20, label='Contact Number')
    company_location = forms.CharField(max_length=100, label='Company Location/Address')
    industry = forms.CharField(max_length=100, label='Industry/Sector')
    username = forms.CharField(max_length=50, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    company_description = forms.CharField(widget=forms.Textarea, label='Company Description or Summary')

class EmployeeRegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email Address')
    contact_number = forms.CharField(max_length=20, label='Contact Number')
    address = forms.CharField(max_length=100, label='Address')
    job_title = forms.CharField(max_length=100, label='Job Title')
    username = forms.CharField(max_length=50, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')