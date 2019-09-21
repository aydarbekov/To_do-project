from django import forms
from django.forms import widgets

status_choices = [('new', 'Новая'),('in_progress', 'В процессе'),('done', 'Сделано')]
class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Описание')
    full_descr = forms.CharField(max_length=3000, required=True, label='Подробное описание')
    status = forms.ChoiceField(required=False, widget=forms.Select, choices=status_choices)
    date = forms.DateField(label='Дата выполнения', required=True, widget=forms.SelectDateWidget)



