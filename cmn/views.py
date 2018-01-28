from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Post, Backup

def posts(request):
    template = 'cmn/post_list.html'
    posts = Post.objects.filter(schvalene=True)
    return render(request, template, {'posts':posts})

def new(request):
    template = 'cmn/post_new.html'
    posts = Post.objects.all()
    if request.method == "POST":
        Post.objects.create(author=request.user, obsah=request.POST['text'], cas=timezone.now(), schvalene=False)
        return redirect('/posts')
    else:
        return render(request, template, {'posts':posts})

def manager(request):
    template = 'cmn/manager.html'
    posts = Post.objects.filter(schvalene=False)
    return render(request, template, {'posts':posts})

def approve(request, url):
    template = 'cmn/approve.html'
    post = Post.objects.get(pk=url)
    if request.method == "POST":
        if 'approve' in request.POST:
            post.schvalene = True
            post.save()
            return redirect('/manager')
        elif 'delete' in request.POST:
            Backup.objects.create(author=post.author, obsah=post.obsah, cas=post.cas, schvalene=False)
            post.delete()
            return redirect('/manager')
        else:
            m = 'neuspesne'
            return render(request, template, {'post':post, 'm':m})
    else:
        return render(request, template, {'post':post})

def index(request):
    template = 'cmn/index.html'
    return render(request, template, {})
