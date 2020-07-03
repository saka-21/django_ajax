from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from .forms import PostAddForm  # 追加
from django.template.loader import render_to_string
from django.http import JsonResponse


def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'app/index.html', {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    liked = False
    if post.like.filter(id=request.user.id).exists():
        liked = True
    return render(request, 'app/detail.html', {'post': post, 'liked': liked})


def like(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        liked = False
    else:
        post.like.add(request.user)
        liked = True
    context = {
        'post': post,
        'liked': liked,
    }
    if request.is_ajax():
        html = render_to_string('app/like.html', context, request=request)
        return JsonResponse({'form', html}, safe=False)


def add(request):
    if request.method == "POST":
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('app:index')
    else:
        form = PostAddForm()
    return render(request, 'app/add.html', {'form': form})


def edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostAddForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('app:detail', post_id=post.id)
    else:
        form = PostAddForm(instance=post)
    return render(request, 'app/edit.html', {'form': form, 'post': post})


def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('app:index')
