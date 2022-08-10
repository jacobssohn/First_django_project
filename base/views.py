from django.shortcuts import render
from django.views.generic.list import  ListView
from django.views.generic.detail import  DetailView
from . models import Task
# from django.http import HttpResponse

class TaskList(ListView):
    model = Task
    context_object_name = 'zadania'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task_det2.html'

