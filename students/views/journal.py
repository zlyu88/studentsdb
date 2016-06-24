# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Views for journal

def journal(request):
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
    return render(request, 'students/journal.html', {'students': students})