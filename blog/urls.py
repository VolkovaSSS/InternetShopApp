from django.urls import path
from blog.views import (
    BlogRecordDetailView,
    BlogRecordListView,
    BlogRecordCreateView,
    BlogRecordUpdateView,
    BlogRecordDeleteView,
)
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("/", BlogRecordListView.as_view(), name="blogrecord_list"),
    path("/<int:pk>/", BlogRecordDetailView.as_view(), name="blogrecord_detail"),
    path("/create/", BlogRecordCreateView.as_view(), name="blogrecord_create"),
    path("/<int:pk>/update/", BlogRecordUpdateView.as_view(), name="blogrecord_update"),
    path("/<int:pk>/delete/", BlogRecordDeleteView.as_view(), name="blogrecord_delete"),
]
