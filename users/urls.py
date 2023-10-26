from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # default auth urls
    path('', include('django.contrib.auth.urls')),
    # registration page
    path('registration', views.registration, name='registration'),
    # employer registration url
    path('employer-registration/', views.employer_registration, name='employer_registration'),
     # Employee registration URL
    path('employee-registration/', views.employee_registration, name='employee_registration'),
]