from django.shortcuts import render, redirect
from myblog.models import PostTag, Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def posts_paginator(request, posts):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts_page = paginator.page(page_number)
    except PageNotAnInteger:
        posts_page = paginator.page(1)
    except EmptyPage:
        posts_page = paginator.page(paginator.num_pages)
    return posts_page


def view_all_posts_action(request):
    posts = Post.objects.all().order_by('datetime').reverse()
    posts_page = posts_paginator(request, posts)

    posts_recent = posts.order_by('datetime').reverse()[:10]
    tags = PostTag.objects.all()
    context = {'posts': posts_page, 'tags': tags, 'recent': posts_recent}
    return render(request, "myblog/all_posts.html", context)


def view_post_action(request, postID):
    post = Post.objects.get(id=postID)
    context = {'post': post}
    return render(request, "myblog/post.html", context)


# def like_post_action(request, postID):
#     post = Post.objects.get(id=postID)
#     post.likes = post.likes + 1
#     post.save()
#     return redirect('post', postID)


def filter_post_action(request, tagID):
    posts = Post.objects.filter(tags__in=[tagID]).order_by('datetime').reverse()
    posts_page = posts_paginator(request, posts)

    posts_recent = Post.objects.all().order_by('datetime').reverse()[:10]
    tags = PostTag.objects.all()
    tag = PostTag.objects.get(id=tagID)
    message1 = "Showing posts with tag: "
    message2 = tag.name
    context = {'posts': posts_page, 'tags': tags, 'recent': posts_recent, 'message1': message1, 'message2': message2}
    return render(request, "myblog/filter_post.html", context)


def home_page_action(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "myblog/background.html", context)

def about_me_action(request):
    posts = Post.objects.filter(tags__in=[3]).order_by('datetime').reverse()[:4]
    context = {'posts': posts}
    return render(request, "myblog/about_me.html", context)
