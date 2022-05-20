from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length','is_public', 'created_at', 'updated_at']
    list_display_links= ['message']
    list_filter = ['created_at','is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width:32px" />')


    def message_length(self, post):
        return len(post.message)
    message_length.short_description = "메시지 글자수"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass