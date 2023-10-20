from django.shortcuts import render
from .models import Job

def index(request):
    # the home page for the app
    return render(request, "job_board/index.html")

def jobs(request):
    # show all jobs available
    jobs = Job.objects.order_by("date_added")
    context = {"jobs": jobs}
    return render(request, "job_board/jobs.html", context)
