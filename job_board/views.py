from django.shortcuts import render
from .models import Job

def index(request):
    jobs = Job.objects.all()[0:3]
    # the home page for the app
    return render(request, "job_board/index.html", {'jobs': jobs})

def jobs(request):
    # show all jobs available
    jobs = Job.objects.order_by("date_posted")
    context = {"jobs": jobs}
    return render(request, "job_board/jobs.html", context)

def job(request, job_id):
    # show a single job and its info
    job = Job.objects.get(id=job_id)
    context = {"job": job}
    return render(request, "job_board/job.html", context)
