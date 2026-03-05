from django.forms import ModelForm
from .models import Task
from django import forms


class Taskform(ModelForm):

    class Meta:
        model = Task
        fields = ['title','complete']

        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Add a new task...'
            })
        }
