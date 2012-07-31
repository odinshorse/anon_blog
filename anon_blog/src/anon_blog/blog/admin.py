from blog.models import Post, Comment
from django.contrib import admin



class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created')
    list_filter = ['created']
    search_fields = ['title']
    date_heirarchy = 'created'
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created')
    list_filter = ['created']
    search_fields = ['title']
    date_heirarchy = 'created'
    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)