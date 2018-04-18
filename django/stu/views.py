from django.shortcuts import render, redirect
from stu.models import Job, Application, Company, Student
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.


def student_index(request):
	# student = Student.objects.get(pk=3)
	if request.session.get('student_id',None)==None:
		return redirect('stu:login')

	student = Student.objects.get(pk=request.session['student_id'])
	applications = student.application_set.all()
	jobs = Job.objects.all()
	applied_jobs = [a.job_id for a in applications]
	new_jobs = set(jobs).difference(applied_jobs)
	companies = Company.objects.all()
	return render(request, 'student/index.html',
				  {'student': student, 'applications': applications, 'jobs': new_jobs, 'companies': companies})


def company_details(request, com_name):
	if request.session.get('student_id',None)==None:
		return redirect('stu:login')
	student = Student.objects.get(pk=request.session['student_id'])
	company = Company.objects.get(name=com_name)
	jobs = company.job_set.all()
	applications = student.application_set.all()
	applied_jobs = [a.job_id for a in applications]
	new_jobs = set(jobs).difference(applied_jobs)
	return render(request, 'company/index.html',
				  {'student': student, 'jobs': jobs, 'new_jobs': new_jobs, 'company': company})


# return HttpResponse("Hello, world. You're at the polls index.")

def apply(request, job_id, stu_id):
	app = Application.objects.create(student_id=Student.objects.get(pk=stu_id), job_id=Job.objects.get(pk=job_id),
									 status='Applied')
	# print(app)
	return redirect('stu:home')


# return HttpResponse("<h3>applied</h3>")
# return redirect('stu_index')

def check(request):
	user = Student.objects.get(email=request.POST['email'])
	if user.password == request.POST['password']:
		request.session['student_id'] = user.id
		return redirect('stu:home')
	return HttpResponse("<p>login error</p>")
	# return redirect('stu:login')

def login(request):
	return render(request, 'company/login_form.html')

def logout(request):
	del request.session['student_id']
	request.session.modified = True
	return redirect('stu:login', permanent=True)


def company_index(request):
	company = Company.objects.get(pk=2)
	jobs = company.job_set.all()
	return render(request, 'company/index.html', {'jobs': jobs})

def job_delete(request, job_id):
	Job.objects.filter(id=job_id).delete()
	return redirect('stu:company_home')

def job_add(request):

	# replace Company.objectsget(id=2) by company's session variable
	add = Job.objects.create(pos=request.POST.get('pos',''),company=Company.objects.get(id=2),skills=request.POST.get('skills',''))
	return redirect('stu:company_home')

class JobCreate(CreateView):
	template_name = "company/job_form.html"
	model = Job
	fields = ['pos', 'skills']

class CompanyView(generic.ListView):
	template_name = 'company/index.html'
	context_object_name = 'jobs'
	def get_queryset(self):
		company = Company.objects.get(pk=2)
		return company.job_set.all()

# class LogIn(CreateView):
#     template_name = "company/login_form.html"
#     model = Student
#     fields = ['name', 'email', 'photo']