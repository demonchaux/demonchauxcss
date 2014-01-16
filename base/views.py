from django.shortcuts import render
from base.models import Post

def home(request):
    context = {'title': 'Website Mockup'}
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'base/index.html', context)

def post_detail(request, post_id):
    context = {'title': 'Frameless Test | spinline.net'}
    post = Post.objects.get(id=post_id)
    context['post'] = post
    return render(request, 'base/contentpage.html', context)
