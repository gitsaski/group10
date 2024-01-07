"""defines URL patterns for job_board"""

from django.urls import path
from . import views

app_name = "job_board"

urlpatterns = [
    # home page
    path("", views.index, name="index"),
    # page for the jobs
    path("jobs/", views.jobs, name="jobs"),
    # page for a single job
    path("jobs/<int:job_id>/", views.job, name="job"),
    # page for applying a job
     path("jobs/<int:job_id>/apply/", views.job_apply, name="job_apply"),
    # page for successful application submit
    path("submit-application-success/", views.submit_application_success, name="submit_application_success")
]
