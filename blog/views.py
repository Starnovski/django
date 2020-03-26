from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def post_index(request):
    posts = Post.objects.all()
    return render(request, '../templates/post_index.html', {'posts':posts})

def post_show(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, '../templates/post_show.html', {'post':post})
