from django.contrib import admin
from .models import Category, Post, SettingWebsite

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_display_links = ["title"]

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "category"]
    list_display_links = ["title"]
    list_filter = ["category"]


admin.site.register(Post, PostAdmin)

admin.site.register(SettingWebsite)
