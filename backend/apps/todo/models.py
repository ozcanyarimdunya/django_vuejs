from django.db import models
from django.urls import reverse


class Todo(models.Model):
    name = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('todo:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('todo:update', args=(self.pk,))
