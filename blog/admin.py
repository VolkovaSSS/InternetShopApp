from django.contrib import admin
from blog.models import BlogRecord


@admin.register(BlogRecord)
class BlogRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "is_published", "views_count")
    list_filter = ("is_published",)
    search_fields = ("title", "content")
    readonly_fields = ("created_at", "views_count")
