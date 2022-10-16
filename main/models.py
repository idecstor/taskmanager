from django.db import models
import sys


class Task(models.Model):
    title = models.CharField('Task name', max_length=50)
    task = models.TextField('Description', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'