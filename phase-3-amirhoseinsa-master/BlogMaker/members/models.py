from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from Blog.models import Blog


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=200)
    blog_n = models.ForeignKey(Blog)

    @staticmethod
    def make_hash(raw_text):
        import hashlib
        hash_object = hashlib.sha512(str(raw_text).encode())
        hex_dig = hash_object.hexdigest()
        return str(hex_dig)[0:150]

    @staticmethod
    def create_user_info(user, current_blog):
        hash_key = UserInfo.make_hash(str(user.username))
        return UserInfo.objects.create(user=user, token=hash_key, current_blog=current_blog)

    def __str__(self):
        return self.user.username + ' - ' + str(self.token)[0:10] + ' ...' + ' - ' + str(self.blog_n.name)
