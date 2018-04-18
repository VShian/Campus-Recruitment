from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'stu'

urlpatterns = [
	url(r'^$', views.student_index, name='home'),
	url(r'^apply/(?P<job_id>[0-9]+)/(?P<stu_id>[0-9]+)/$', views.apply, name='apply'),
	url('check', views.check, name='check'),
	url(r'^company/(?P<com_name>[A-Za-z]+)$', views.company_details, name='company_details'),
	# url(r'^cmp$', views.company_index, name='company_home'),
	url(r'^company-home$', views.CompanyView.as_view(), name='company_home'),
	url(r'delete/(?P<job_id>[0-9]+)$', views.job_delete,name='delete'),
	url(r'job/add/1$', views.JobCreate.as_view(), name='job-add'),
	url(r'login$', views.login, name='login'),
	url(r'XsDfrA$', views.logout, name='logout'),	#url is such that no one can guess it
	# url(r'login$', views.LogIn.as_view(), name='login'),
	url(r'job/added$', views.job_add, name='job-added'),


]