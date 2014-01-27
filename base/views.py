from django.shortcuts import render
from base.models import Post, PostImage, Event

def home(request):
    context = {'title': 'Website Mockup'}
    posts = Post.objects.all().order_by('?')
    context['posts'] = posts
    context['events'] = Event.objects.all().order_by('-timestamp')[:10]
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
        posts = Post.objects.filter(post_type=param).order_by('?')
    else:
        posts = Post.objects.all().order_by('?')
    context['posts'] = posts
    context['filter'] = True
    context['events'] = Event.objects.all().order_by('-timestamp')[:10]
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
    return render(request, 'base/biography.html', {})

def event_detail(request, event_id):
    context = {}
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        event = None
    context['event'] = event
    return render(request, 'base/event_content.html', context)