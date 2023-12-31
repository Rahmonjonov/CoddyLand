from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('program/', program_view, name='program'),
    path('article/', article_view, name='article'),
    path('blog/<int:pk>/', blog_view, name='blog'),
]