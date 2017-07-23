from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login, name='sign_in'),
    url(r'^register/', views.sign_up, name='sign_up'),
    url(r'^blog_id/', views.blog_idg, name='get_home_blog_id'),
    url(r'^test/', views.tt, name='test'),
]
