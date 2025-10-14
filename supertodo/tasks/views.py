from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddTaskForm, EditTaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task/list.html', {'tasks': tasks})


def task_list_completed(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'tasks/task/completed.html', {'tasks': tasks})


def task_list_pending(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, 'tasks/task/pending.html', {'tasks': tasks})


def task_detail(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/task/detail.html', {'task': task})


def add_task(request):
    if request.method == 'POST':
        if (form := AddTaskForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    else:
        form = AddTaskForm()
    return render(request, 'tasks/task/add.html', dict(form=form))


def delete_task(request):
    return redirect('tasks:task-list')


def edit_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    if request.method == 'POST':
        if (form := EditTaskForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    else:
        form = EditTaskForm(instance=task)
    return render(request, 'tasks/task/edit.html', dict(task=task, form=form))


def toogle_task(request):
    Task.completed = not Task.completed
    Task.completed.save()
