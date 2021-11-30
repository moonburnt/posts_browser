from django.contrib import admin

from user_browser.models import UsersModel, PostsModel
# Register your models here.

admin.site.register(UsersModel)
admin.site.register(PostsModel)
