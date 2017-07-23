from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<blog_id>[0-9]+)/posts/', views.postsg, name='get_posts'),
    url(r'^(?P<blog_id>[0-9]+)/post/', views.postg, name='get_post'),
    url(r'^comments/', views.commentsg, name='get_comments'),
    url(r'^comment/', views.comment_c, name='add_comments'),
]