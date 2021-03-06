from csv import list_dialects
from xml.etree.ElementTree import Comment
from django.contrib import admin
from jmespath import search
from .models import Post
from django.utils.safestring import mark_safe
# Register your models here.

#admin.site.register(Post) 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','photo_tag', 'message','message_length','is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at','is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}"style="width: 70px;" />' )
        return None
#admin.site.register(Post, PostAdmin)
    def message_length(self, post):
        return " 글자"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass