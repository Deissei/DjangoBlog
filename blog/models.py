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
    