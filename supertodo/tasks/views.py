from django.shortcuts import render

from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task/list.html', {'tasks': tasks})


# def task_list_pending():
# def task_list_completed():
# def add_task():
# def task_detail():
# def delete_task():
# def edit_task():
# def toogle_task():
