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
    posts = Post.objects.all()[::-1] # Из нашей моделки возьми все объекты
    
    try:
        settings = SettingWebsite.objects.get(id=1)
    except SettingWebsite.DoesNotExist:
        return render(request, "index.html", locals())
    
    return render(request, "index.html", locals())


def detail_post(request, post_id):
    try:
        settings = SettingWebsite.objects.get(id=1)
    except SettingWebsite.DoesNotExist:
        return render(request, "post.html", locals())
    
    post = Post.objects.get(id=post_id)
    
    categories = Category.objects.all()
    
    new_post = Post.objects.all()[::-1][:3]
    
    return render(request, "post.html", locals())


def seacrh(request):
    if request.method == "GET":
        query = request.GET["query"]
        
        try:
            settings = SettingWebsite.objects.get(id=1)
        except SettingWebsite.DoesNotExist:
            return render(request, "seacrh.html", locals())
        
        if query:
            posts = Post.objects.filter(title__icontains=query)


        
        return render(request, "seacrh.html", locals())
