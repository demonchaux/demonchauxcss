from django.shortcuts import render
from base.models import Post, PostImage, POST_TYPES

def home(request):
    context = {'title': 'Website Mockup'}
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'base/index.html', context)

def home_filter(request, type=''):
    context = {'title': 'Website Mockup'}
    params = {
        'software': 'a',
        'projects': 'd',
        'design': 'c',
        'books': 'b'
    }
    param = params.get(type, '')
    if param:
        posts = Post.objects.filter(post_type=param)
    else:
        posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'base/index.html', context)

def post_detail(request, post_id):
    context = {'title': 'Frameless Test | spinline.net'}
    post = Post.objects.get(id=post_id)
    images = []
    if post:
        images = PostImage.objects.filter(post_id=post.id)
    context['post'] = post
    context['images'] = images
    return render(request, 'base/contentpage.html', context)

def biography(request):
    context = {}
    return render(request, 'base/biography.html', context)
