from django.contrib import admin

# Register your models here.
from members.models import UserInfo

admin.site.register(UserInfo)
