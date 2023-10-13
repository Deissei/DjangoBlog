from django.contrib import admin
from .models import Category, Post, SettingWebsite

admin.site.register(Category)
admin.site.register(Post)

admin.site.register(SettingWebsite)
