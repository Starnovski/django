from django.shortcuts import render
from .models import Post

# Create your views here.


def post_index(request):
    posts = Post.objects.all()
    return render(request, '../templates/post_index.html', {'posts':posts})
