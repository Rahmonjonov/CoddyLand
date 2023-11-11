from django.shortcuts import render
from .models import *


def index_view(request):
    context = {
        'article':Article.objects.all()
    }
    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def program_view(request):
    return render(request, 'dasturlar.html')

def article_view(request):
    context = {
        'article':Article.objects.all()
    }
    return render(request, 'maqolalar.html', context)

def blog_view(request, pk):
    context = {
        'article':Article.objects.get(id=pk),
    }
    return render(request, 'single_blog_page.html', context)