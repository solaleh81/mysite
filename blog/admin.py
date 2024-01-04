from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    # fields = ('title',)
    list_display = ["title", "content", "counted_views", "created_date", "status"]
    list_filter = ("status",)
    ordering = ['created_date']
    search_fields = ['title', 'content']
# admin.site.register(Post)