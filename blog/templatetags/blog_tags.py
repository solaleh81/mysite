from django import template

from blog.models import Post

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.all().count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.all().count()
    return posts