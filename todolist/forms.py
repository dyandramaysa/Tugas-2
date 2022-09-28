from django.forms import ModelForm
from .models import Task
from django import forms

class CreateTask(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']