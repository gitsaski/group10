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

def job_apply(request, job_id):
    # Your logic for handling job applications goes here
    job = Job.objects.get(pk=job_id)
    return render(request, 'job_board/job_apply.html', {'job': job})
