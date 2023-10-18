from django.urls import path
from .views import create_post, homepage, detail_post, seacrh

urlpatterns = [
    path('', homepage, name="homepage"),
    path('create_post/', create_post, name="create_post"),
    path('posts/<int:post_id>', detail_post, name="detail_post"),
    path('seacrh/', seacrh, name="seacrh"),
]
