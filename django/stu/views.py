from django.shortcuts import render
from .models import *
# from django.http import HttpResponse

# Create your views here.
def index(request):
    student = Student.objects.get(pk=1)
    applications = student.application_set.all()
    jobs = Job.objects.all()
    companies = Company.objects.all()
    return render(request, 'index.html', {'applications' : applications, 'jobs' : jobs, 'companies' : companies })


def display(request):
    return render(request, 'index.html', {})
    # return HttpResponse("Hello, world. You're at the polls index.")
