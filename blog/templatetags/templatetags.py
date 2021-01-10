from django import template
from ..models import Post, Comment

register = template.Library()

@register.simple_tag
def total():
    post = Post.objects.all()
    return post.count()

@register.simple_tag
def total_comments():
    comment = Comment.objects.all()
    return comment.count()
