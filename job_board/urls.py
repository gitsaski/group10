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
    path("jobs/<int:job_id>/", views.job, name="job")
]