from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from posts.forms import CommentForm, PostCreateForm
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
    return render(request, "posts/feed.html", {"posts": myPosts, "title": "My Posts"})


@login_required
def feed(request):
    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            newComment = commentForm.save(commit=False)
            postId = request.POST.get('post_id')
            newComment.posted_by = request.user
            post = get_object_or_404(Post, id=postId)
            newComment.post = post
            newComment.save()
    commentForm = CommentForm()
    posts = Post.objects.all().order_by("-created")
    return render(
        request,
        "posts/feed.html",
        {"posts": posts, "title": "All Posts", 'comment_form': commentForm},
    )


@login_required
def like_post(request):
    post_id = request.POST.get("post_id")
    post = get_object_or_404(Post, id=post_id)
    if post.liked_by.filter(id=request.user.id):
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect('index')
