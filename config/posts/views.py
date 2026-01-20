from django.shortcuts import render
# Create your views here.

def index(request):
    posts = [
        {"title": "最初の投稿"},
        {"title": "Django楽しい"},
        {"title": "SSR理解できた"},
    ]

    user_message = ""
    bot_message = ""

    if request.method == "POST":
        user_message = request.POST.get("message","") .strip()

        bot_message = f"受け取ったよ : {user_message}"

    return render(request, "posts/index.html",{
        "title": "Posts",
        "message": "Django テンプレート最高",
        "posts" : posts,
        "user_message": user_message,
        "bot_message": bot_message,
    })