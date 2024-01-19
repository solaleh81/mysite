from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def blog_view(request, **kwargs):
    posts = Post.objects.all()
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    return render(request, 'blog/blog-home.html', context={'posts': posts})


def blog_single(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context=context)


def test(request):
    posts = Post.objects.filter(status=1)
    return render(request, 'test.html', context={'posts': posts})


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    return render(request, 'blog/blog-home.html', context={'posts': posts})


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    return render(request, 'blog/blog-home.html', context={'posts': posts})
