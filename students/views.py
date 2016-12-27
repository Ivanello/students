# -*- coding: utf-8 -*-

# from django.http import Http404 
# from django.http import HttpResponse

# def students_list(request): 
# 	# try:
# 	# 	sid = int(sid) 
# 	# except ValueError:
# 	# 	raise Http404 
# 	# else:
# 		return HttpResponse('<h1>Hello World!!!</h1>')


# from django.shortcuts import render 
# from django.http import HttpResponse
# def students_list(request):
# 	return HttpResponse('<h1>Hello World</h1>')


# from django.http import HttpResponse
# from django.template import RequestContext, loader
# def students_list(request):
# 	template = loader.get_template('demo.html') 
# 	context = RequestContext(request, {})
# 	return HttpResponse(template.render(context))

from django.shortcuts import render 
from django.http import HttpResponse

#Students

def students_list(request):
	students = (
        {'id': 1,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'ticket': 235,
         'image': 'img/1.jpg'},
        {'id': 2,
         'first_name': u'Корост',
         'last_name': u'Андрій',
         'ticket': 2123,
         'image': 'img/me.jpg'},
		{'id': 3,
         'first_name': u'Іван',
         'last_name': u'Майдан',
         'ticket': 212,
         'image': 'img/me.jpg'},)
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('<h1>Student add form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Student %s edit form</h1>' %sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Student %s del form</h1>' %sid)

#Groups

def groups_list(request):
	return HttpResponse('<h1>Groups list</h1>',)

def groups_add(request):
	return HttpResponse('<h1>Groups add form</h1>')

def groups_edit(request, sid):
	return HttpResponse('<h1>Edit group %s</h1>' %sid)

def groups_delete(request, sid):
	return HttpResponse('<h1>Del Group %s</h1>' %sid)

#Journal

def journal(request):
	return HttpResponse('<h1>Journal</h1>',)

def journal_update(request):
	return HttpResponse('<h1>Journal updated</h1>')

def journal_personal(request, sid):
	return HttpResponse('<h1>Journal of  %s student </h1>' %sid)