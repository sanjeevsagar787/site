from django.shortcuts import render, HttpResponse,redirect
from Blogs.models import Post
from django.contrib import messages

# Create your views here.
def blogHome(request):
    mypost = Post.objects.all()
    return render(request, 'blog/blogHome.html', {'mypost':mypost}) 

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug)
    return render(request, 'blog/blogPost.html', {'post':post})     

