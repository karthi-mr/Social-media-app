from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from posts.forms import PostCreateForm
from posts.models import Post


@login_required
def post_create(request):
    if request.method == 'POST':
        postForm = PostCreateForm(request.POST, files=request.FILES)
        if postForm.is_valid():
            newPost = postForm.save(commit=False)
            newPost.user = request.user
            newPost.save()
    else:
        postForm = PostCreateForm()
    return render(request, "posts/create.html", {"post_form": postForm})


@login_required
def my_posts(request):
    currentUser = request.user
    myPosts = Post.objects.filter(user=currentUser)
    return render(request, "posts/my_posts.html", {"my_posts": myPosts})


@login_required
def feed(request):
    posts = Post.objects.all().order_by("-created")
    return render(request, "posts/feed.html", {"posts": posts})
