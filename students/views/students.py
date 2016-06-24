# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Views for Students

def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Бутч',
         'last_name': u'Кулідж',
         'ticket': 529,
         'image': 'img/бутч.jpg'},
        {'id': 2,
         'first_name': u'Бендер',
         'last_name': u'Родріґез',
         'ticket': 128,
         'image': 'img/бендер.gif'},
        {'id': 3,
         'first_name': u'Гомер',
         'last_name': u'Сімпсон',
         'ticket': 502,
         'image': 'img/гомер.jpg'},
    )
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)