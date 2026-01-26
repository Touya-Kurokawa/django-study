from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        if request.method == "POST":
            data = json.loads(request.body)
            message = data.get('message', '')

            replay = f"APIで受け取ったよ : {message}"

            return JsonResponse({
                "reply": replay
            }, json_dumps_params={'ensure_ascii': False})
        return JsonResponse({
            "error": "POST only"
        }, status=405)

def index(request):
    posts = [
        {"title": "最初の投稿"},
        {"title": "Django楽しい"},
        {"title": "SSR理解できた"},
    ]

    if request.method == "POST":
        user_message = request.POST.get("message", "") .strip()
        bot_message = f"受け取ったよ : {user_message}"

        request.session["user_message"] = user_message
        request.session["bot_message"] = bot_message
        
        return redirect("posts:index")

    user_message = request.session.pop("user_message", "")
    bot_message = request.session.pop("bot_message", "")

    return render(request, "posts/index.html",{
        "title": "Posts",
        "message": "Django テンプレート最高",
        "posts" : posts,
        "user_message": user_message,
        "bot_message": bot_message,
    })