from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'stu'

urlpatterns = [
	url(r'^$', views.student_index, name='home'),
	url(r'^apply/(?P<job_id>[0-9]+)/(?P<stu_id>[0-9]+)/$', views.apply, name='apply'),
	url('check', views.check, name='check'),
	url(r'^company/(?P<com_name>[A-Za-z]+)$', views.company_details, name='company_details'),

]