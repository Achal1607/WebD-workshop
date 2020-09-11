from django.contrib import admin 
# Register your models here.
from .models import UserInfo
from .models import InstituteInfo
admin.site.register(UserInfo)
admin.site.register(InstituteInfo)
