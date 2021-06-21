from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    photo = models.ImageField()
    published_date = models.DateTimeField(auto_now_add=True)
    caption = models.TextField(max_length=200)

    def __str__(self):
        return self.caption

    @staticmethod
    def get_absolute_url():
        return reverse('posts')
