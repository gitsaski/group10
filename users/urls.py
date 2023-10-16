from django.urls import path
from . import views

urlpatterns = [
    path('employer-registration/', views.employer_registration, name='employer_registration'),
]