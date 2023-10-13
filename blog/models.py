from typing import Any
from django.db import models


class Category(models.Model):
    """ Модель(Таблица Категории)
    """
    title = models.CharField(
        max_length=255,
    )
    
    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    """ Модель(Таблица Поста)
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to="posts/",
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        max_length=2000,
    )
    created_at = models.DateField(
        auto_now_add=True,
    )
    author = models.CharField(
        max_length=30,
    )
    
    def __str__(self):
        return f"{self.title}"


class SettingWebsite(models.Model):
    title = models.CharField(
        max_length=10,
    )
    description = models.CharField(
        max_length=100,
    )
    director = models.CharField(
        max_length=30
    )
    
    facebook_url = models.URLField(
        null=True,
        blank=True,
    )
    twitter_url = models.URLField(
        null=True,
        blank=True,
    )
    instagram_url = models.URLField(
        null=True,
        blank=True,
    )
    linkendin_url = models.URLField(
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return f"{self.title}"
