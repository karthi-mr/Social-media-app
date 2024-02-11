from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ("title", "slug", "created", "user")
    list_display_links = ("title",)
