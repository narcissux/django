from django.contrib import admin
from . import models
# 注册模型进管理后台
admin.site.register(models.Post)
admin.site.register(models.Tag)
admin.site.register(models.Category)
