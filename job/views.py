from django.shortcuts import render
from .models import Job

def homepage(request):
    return render(request, 'job/home.html', {'jobs': Job.objects})