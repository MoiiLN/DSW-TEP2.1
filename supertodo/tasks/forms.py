from django import forms

from .models import Task


class AddTaskFrom(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'slug')
