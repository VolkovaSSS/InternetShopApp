from django.contrib import admin
from blog.models import BlogRecord


@admin.register(BlogRecord)
class BlogRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title",)
    readonly_fields = ("created_at",)
