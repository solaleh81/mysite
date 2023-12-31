from django.shortcuts import render

def blog_view(request):
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    context = {'title': 'bitcoin crashed again!', 'content': 'bitcoin was flying...'}
    return render(request, 'blog/blog-single.html', context=context)

