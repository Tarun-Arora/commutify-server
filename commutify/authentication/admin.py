from django.contrib import admin

# Register your models here.
from .models import UserInfo, ForgotPwdRequest
admin.site.register(UserInfo)
admin.site.register(ForgotPwdRequest)