from django.shortcuts import render, HttpResponse
import random

import posts
from posts.models import Post


def test_view(request):
    return HttpResponse(f"twinkling watermelon {random.randint(1, 100)}")

def html_view(request):
    return render(request,"main.html")

def post_list_view(request):
    post = (Post.objects.all())
    print(posts)
    return render(request,"posts/post_list.html",{"posts":post})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request,"posts/post_detail.html", {"posts":post})