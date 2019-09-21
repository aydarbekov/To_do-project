from django.db import models

from django.db import models
status_choices = [('new', 'Новая'),('in_progress', 'В процессе'),('done', 'Сделано')]
class Article(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    full_descr = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Подробное описание')
    status = models.CharField(max_length=300, null=False, blank=False, verbose_name='Статус',default=status_choices[0][0], choices=status_choices)
    date = models.DateField(verbose_name='Дата выполнения',null=True, blank=True, default='')

    def __str__(self):
        return self.description

