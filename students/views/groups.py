# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Views for Groups

def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'М-11',
         'leader': u'Бутч Кулідж'},
        {'id': 2,
         'name': u'М-12',
         'leader': u'Бендер Родріґез'},
        {'id': 3,
         'name': u'М-13',
         'leader': u'Гомер Сімпсон'},
    )
    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)