from django.shortcuts import render, redirect
from .models import Category, Post, SettingWebsite

def create_post(request):
    if request.method == "POST":
        category = Category.objects.get(id=request.POST["category"])
        title = request.POST["title"]
        description = request.POST["description"]
        author = request.POST["author"]
        
        Post.objects.create(
            category=category,
            title=title,
            description=description,
            author=author,
        )
        return redirect("/")
    
    if request.method == "GET":
        category = Category.objects.all()
        context = {
            "category": category,
        }
    
    return render(request, "create_post.html", context)


def homepage(request):
    posts = Post.objects.all() # Из нашей моделки возьми все объекты
    
    try:
        settings = SettingWebsite.objects.get(id=1)
    except SettingWebsite.DoesNotExist:
        return render(request, "index.html", locals())
    
    return render(request, "index.html", locals())
