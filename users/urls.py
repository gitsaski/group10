from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    # default auth urls
    path('', include('django.contrib.auth.urls')),
    # registration page
    path('registration/', views.registration, name='registration'),
    # employer registration url
    path('employer-registration/', views.employer_registration, name='employer_registration'),
     # Employee registration URL
    path('employee-registration/', views.employee_registration, name='employee_registration'),
    # Company registration URL
    path('company-registration/', views.company_registration, name='company_registration'),

    path('registration_success_employer/', views.registration_success_employer, name='registration_success_employer'),
    
    path('registration_success_employee/', views.registration_success_employee, name='registration_success_employee'),

    path('registration_success_company/', views.registration_success_company, name='registration_success_company'),
    
    # profile url
    path('profile/', views.profile, name='profile')
]