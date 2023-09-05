from django.forms import ModelForm
from django import forms

from app.models import TODO
# class TODOForm(ModelForm):
#     class Meta:
#         model = TODO
#         fields = ['title' , 'status' ,'due_date', 'priority', 'result']


class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'status', 'due_date', 'priority', 'result', 'category']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.TextInput(attrs={'readonly': 'readonly'}),
        }