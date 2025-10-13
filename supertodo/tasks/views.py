from django.shortcuts import render, redirect

from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task/list.html', {'tasks': tasks})

def task_list_completed(request):
    tasks = Task.objects.filter(task_list_completed=True)
    return render(request, 'tasks/task/list.html'), {'tasks': tasks}

def task_list_pending(request):
    tasks = Task.objects.filter(task_list_completed=False)
    return render(request, 'tasks/task/list.html'), {'tasks': tasks}

def task_detail(request, slug):
     tasks = Task.objects.filter(slug=slug)
     return render(request, 'tasks/task/detail.html', {'tasks': tasks})

def add_task(request):
    pass
def delete_task(request):
    pass
def edit_task(request):
    pass
def toogle_task(request):
    Task.completed = not Task.completed
    Task.save()
    return redirect('list.html')
