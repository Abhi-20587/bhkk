# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import View
from .models import Student
from django.shortcuts import render, redirect
from .forms import AddStudentForm


class Home_g(View):
    def get(self,request):
        jr=Student.objects.all()
        return render(request,'home/abhitable.html',{'ab':jr})

class Add_Student(View):
    def get(self, request):
        fm = AddStudentForm()
        return render(request, 'home/add-student.html', {'form':fm})
    
    
    def post(self, request): 
        fm=AddStudentForm(request.POST)
        if (fm == ""):
            return render(request, 'home/add-student.html', {'error':fm})
        else:
            fm.save()
            return redirect('/')
        # else:
        #     return render(request, 'core/add-student.html', {'form':fm})
    
class Delete_Student(View):
    def post(self, request):
        data = request.POST
        id=data.get('id')
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/')

class EditStudent(View):
    def get (self,request,id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(instance=stu)
        return render(request, 'home/edit-student.html', {'form':fm})
    def post (self,request,id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
        return redirect ('/')


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
