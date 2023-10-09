from django.urls import path
from .views import create_post

urlpatterns = [
    path('create_post/', create_post, name="create_post"),
]


# Создать функцию которая показывает index.html

# Добавишь путь что бы пользователь после захода в главную странцу показывался index.html
