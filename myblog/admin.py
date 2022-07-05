from django.contrib import admin
from .models import Post, PostTag


# Register your models here.

@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
