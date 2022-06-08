from django.http import HttpResponse, HttpResponseRedirect
import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Students

def home(request):
    return render(request, "triangles/home.html")

def about(request):
    return render(request, "triangles/about.html")

def contact(request):
    return render(request, "triangles/contact.html")

def a_types(request):
    return render(request, "triangles/a_types.html")

def t_types(request):
    return render(request, "triangles/t_types.html")

def t_area(request):
    return render(request, "triangles/t_area.html")

def triangle_angles(request, name):
    return render(
        request,
        'triangles/triangle_angles.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def students(request):
  mystudents = Students.objects.all().values()
  template = loader.get_template('students.html')
  context = {
    'mystudents': mystudents,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('triangles/add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['firstname']
  y = request.POST['lastname']
  e = request.POST['email']
  t = request.POST['textarea']
  student = Students(firstname=x, lastname=y, email=e, textarea=t)
  student.save()
  return HttpResponseRedirect(reverse('students'))

def delete(request, id):
  member = Students.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('students'))

def update(request, id):
  mystudents = Students.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mystudents': mystudents,
  }
  return HttpResponse(template.render(context, request))
  
