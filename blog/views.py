from django.shortcuts import render
from blog.models import Post
def blog_view(request):
    posts = Post.objects.filter(status=0)
    return render(request, 'blog/blog-home.html', context={'posts': posts})

def blog_single(request, id):
    post = Post.objects.get(pk=id)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context=context)

def test(request):
    posts = Post.objects.filter(status=0)
    return render(request, 'test.html', context={'posts': posts})