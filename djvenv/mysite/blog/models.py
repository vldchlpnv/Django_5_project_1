from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)  # дата создания
    created = models.DateTimeField(auto_now_add=True)  # дата публикации
    updated = models.DateTimeField(auto_now=True) # дата изменения

    class Meta:

        indexes = [models.Index(fields=['-publish'])]
        ordering = ['-publish'] # сортировка от новых с старым

    def __str__(self):
        return self.title

