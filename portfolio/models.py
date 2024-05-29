from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    slug = models.SlugField(unique=True, max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.URLField(max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateField(auto_now_add=True)
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} - {self.date_published}'

    class Meta:
        ordering = ['-date_published']  


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    image_url = models.URLField(max_length=200)
    caption = models.TextField(blank=True)

    def __str__(self):
        return self.image_url
