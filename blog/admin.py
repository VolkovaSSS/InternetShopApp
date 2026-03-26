from django.contrib import admin
from blog.models import BlogRecord


@admin.register(BlogRecord)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "is_published")
    # list_filter = ("category",)
    search_fields = ("title")
    readonly_fields = ("created_at")
