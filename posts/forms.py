from django import forms

from posts.models import Comment, Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "caption", "image")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
