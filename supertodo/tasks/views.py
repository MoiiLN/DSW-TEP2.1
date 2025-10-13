from .models import Task


def task_list(request):
    tasks = Task.objects.all()
