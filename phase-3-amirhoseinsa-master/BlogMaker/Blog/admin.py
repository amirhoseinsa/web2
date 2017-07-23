from django.contrib import admin

# Register your models here.
from Blog.models import Blog, PostComments, BlogPosts

admin.site.register(Blog)
admin.site.register(PostComments)
admin.site.register(BlogPosts)
