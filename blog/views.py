from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import CommentForm
import json
import urllib

# Create your views here.


def post_index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    #url = "http://localhost:3000/api/v1/categories"
    #response = urllib.request.urlopen(url)
    #data = json.loads(response.read())

    return render(request, '../templates/post_index.html', {'page':page, 'posts':posts})


def post_show(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    return render(request, '../templates/post_show.html', {'post':post, 'comments':comments})


def show_category_posts(request, category_id):
    posts = Post.objects.filter(category = category_id)
    return render(request,'../templates/post_index.html',{'posts':posts})


def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_show', pk=pk)
    else:
        form = CommentForm()
    return render(request, '../templates/comment_new.html',{'form':form, 'post':post})
