from django.shortcuts import render

def index(request):
    # the home page for the app
    return render(request, "job_board/index.html")
