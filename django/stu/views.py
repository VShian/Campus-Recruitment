from django.shortcuts import render, redirect
from stu.models import *
from django.http import HttpResponse

# Create your views here.
def student_index(request):
	student = Student.objects.get(pk=3)
	applications = student.application_set.all()
	jobs = Job.objects.all()
	applied_jobs = [a.job_id for a in applications]
	new_jobs = set(jobs).difference(applied_jobs)
	companies = Company.objects.all()
	return render(request, 'student/index.html', {'student':student ,'applications' : applications, 'jobs' : new_jobs, 'companies' : companies })


def company_details(request, com_name):
	student = Student.objects.get(pk=3)
	company = Company.objects.get(name=com_name)
	jobs = company.job_set.all()
	applications = student.application_set.all()
	applied_jobs = [a.job_id for a in applications]
	new_jobs = set(jobs).difference(applied_jobs)
	return render(request, 'company/details.html', {'student':student, 'jobs':jobs, 'new_jobs':new_jobs, 'company':company})
# return HttpResponse("Hello, world. You're at the polls index.")

def apply(request, job_id, stu_id):
	app = Application.objects.create(student_id=Student.objects.get(pk=stu_id), job_id=Job.objects.get(pk=job_id), status='Applied')
	# print(app)
	return redirect('stu:stu_index')
	# return HttpResponse("<h3>applied</h3>")
# return redirect('stu_index')

def check(request):
	return redirect('stu:home')

def company_index(request):
	pass


