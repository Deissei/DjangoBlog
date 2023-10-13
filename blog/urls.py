from django.urls import path
from .views import create_post, homepage

urlpatterns = [
    path('', homepage, name="homepage"),
    path('create_post/', create_post, name="create_post"),
]
