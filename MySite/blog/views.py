from django.shortcuts import render
from django.http import Http404
from .models import Post
from django.shortcuts import get_object_or_404, render
# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(
    request,
    'blog/post/list.html',
    {'posts': posts}
    )

def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
        post = get_object_or_404(
            Post,
            id = id,
            status=Post.Status.PUBLISHED
        )
    except Post.DoesNotExist:
        raise Http404("Nie znaleziono posta.")
    return render(
    request,
    'blog/post/detail.html',
    {'post': post}
    )