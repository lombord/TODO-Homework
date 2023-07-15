from django import forms

from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = TaskModel
        widgets = {
            'deadline': forms.DateTimeInput(attrs={
                'type': 'datetime-local', }),
            'description': forms.Textarea(attrs={'rows': 6})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
