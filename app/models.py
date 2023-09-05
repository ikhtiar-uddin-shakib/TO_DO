from django import forms
from django.db import models
from django.contrib.auth.models import User

class TODO(models.Model):
    status_choices = [
        ('C', 'COMPLETED'),
        ('P', 'PENDING'),
    ]
    priority_choices = [
        ('1', '1️⃣'),
        ('2', '2️⃣'),
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣'),
        ('6', '6️⃣'),
        ('7', '7️⃣'),
        ('8', '8️⃣'),
        ('9', '9️⃣'),
        ('10', '🔟'),
    ]
    CHOICE=[
        ('FITNESS', 'FITNESS'),
        ('STUDY', 'STUDY'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=status_choices, default='P')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField(null=True)
    priority = models.CharField(max_length=2, choices=priority_choices)
    result = models.BooleanField(default=False)
    category = models.CharField(max_length=30, choices=CHOICE, null=True)

    def __str__(self):
        return str(self.title)

# class TODOForm(forms.ModelForm):
#     class Meta:
#         model = TODO
#         fields = ['title', 'status', 'user', 'due_date', 'priority', 'result']
#         widgets = {
#             'due_date': forms.DateInput(attrs={'type': 'date'}),
#         }
