from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=0)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    return render(request, 'blog/blog-home.html', context={'posts': posts})


def blog_single(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context=context)


def test(request):
    posts = Post.objects.filter(status=0)
    return render(request, 'test.html', context={'posts': posts})


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=0)
    posts = posts.filter(category__name=cat_name)
    return render(request, 'blog/blog-home.html', context={'posts': posts})
