from django.shortcuts import render, redirect
from main.urls import *
from .models import *

def index_view(request):
    context = {
        'banner':Banner.objects.all().order_by('-id')[:2],
        'support':Support.objects.last(),
        'image':Image.objects.all().order_by('-id')[:2],
        'arrivals':Product.objects.all().order_by('-id')[:16],
        'blog':Blog.objects.all().order_by('-id')[:4]

    }
    return render(request, 'index.html', context )

def shop_view(request):

    return render(request, 'shop-left-sidebar.html' )


def product_view(request):

    return render(request, 'single-product.html' )

def blog_view(request):
    context = {
            'blog':Blog.objects.all().order_by('-id')[:4],
            'category':Category.objects.all().order_by('-id')[:5],
            'post':Blog.objects.all().order_by('-id')[:3],
        }
    return render(request, 'blog-left-sidebar.html', context)


def single_blog_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog':blog,
        'category': Category.objects.all().order_by('-id')[:5],
        'post': Blog.objects.all().order_by('-id')[:3],
    }

    return render(request, 'single-blog.html', context)


def contact_view(request):

    return render(request, 'contact.html')


def about_view(request):
    context = {
        'about':About.objects.last(),
        'team':Team.objects.all().order_by('-id')[:3]
    }
    return render(request, 'about-us.html', context)