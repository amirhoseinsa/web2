from django.contrib import admin

from .models import *


class BlogAdmin(admin.ModelAdmin):
	# fields = ['owner', 'name']
	list_display = ('name', 'blog_id', 'owner')
	list_filter = ['blog_id', 'owner']
	search_fields = ['name', 'blog_id', 'owner']


class PostAdmin(admin.ModelAdmin):
	# fields = []
	list_display = ('title', 'summary', 'blog')
	list_filter = ['blog']
	search_fields = ['text', 'title', 'summary']


class CommentAdmin(admin.ModelAdmin):
	# fields = []
	list_display = ('post', 'text')
	# list_filter = ['blog_id', 'owner']
	search_fields = ['post', 'text']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
