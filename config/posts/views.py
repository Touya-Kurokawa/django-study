from django.shortcuts import render
# Create your views here.

def index(request):
    posts = [
        {"title": "最初の投稿"},
        {"title": "Django楽しい"},
        {"title": "SSR理解できた"},
    ]

    return render(request, "posts/index.html",{
        "title": "Posts",
        "massage": "Django テンプレート最高",
        "posts" : posts,
    })