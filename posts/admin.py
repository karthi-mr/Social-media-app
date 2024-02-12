from django.contrib import admin

from posts.models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created", "user")
    list_display_links = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "body", "posted_by", "created")
    list_display_links = ("post",)
