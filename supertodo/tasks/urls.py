from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('detail/', views.task_detail, name='task-detail'),
    path('edit/', views.edit_task, name='edit-task'),
    path('delete/', views.delete_task, name='delete-task'),
]
