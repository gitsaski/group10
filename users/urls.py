from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # default auth urls
    path('', include('django.contrib.auth.urls')),
    # employer registration url
    path('employer-registration/', views.employer_registration, name='employer_registration'),
]