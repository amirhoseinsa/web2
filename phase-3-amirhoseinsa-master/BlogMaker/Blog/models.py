from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Blog(models.Model):
    owner = models.ForeignKey(User, default=0)
    id_b = models.AutoField(primary_key='true')
    name = models.CharField(max_length=50)
    last = models.CharField(max_length=100)
    time = models.DateField(auto_now_add='true')
    def __str__(self):
        return str(self.name)


class BlogPosts(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    id_p = models.AutoField(primary_key='true')
    summary = models.CharField(max_length=150)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    owner = models.CharField(max_length=100)
    time = models.DateField(auto_now_add='true')

    def __str__(self):
        return str(self.summary)

    @staticmethod
    def create(blog, title, summary, text):
        return BlogPosts.objects.create(blog=blog, title=title, summary=summary, text=text)


class PostComments(models.Model):
    post = models.ForeignKey(BlogPosts, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    id_C = models.IntegerField()
    time = models.DateField(auto_now_add='true')

    def __str__(self):
        return str(self.text)

    @staticmethod
    def create(post, text):
        return PostComments.objects.create(post=post, text=text)
