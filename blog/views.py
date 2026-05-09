from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import BlogRecord


class BlogRecordListView(ListView):
    model = BlogRecord

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogRecordDetailView(LoginRequiredMixin, DetailView):
    model = BlogRecord

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogRecordCreateView(LoginRequiredMixin, CreateView):
    model = BlogRecord
    fields = ["title", "content", "is_published", "preview"]
    success_url = reverse_lazy("blog:blogrecord_list")


class BlogRecordUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogRecord
    fields = ["title", "content", "is_published", "preview"]
    success_url = reverse_lazy("blog:blogrecord_list")

    def get_success_url(self):
        return reverse("blog:blogrecord_detail", args=[self.kwargs.get("pk")])


class BlogRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogRecord
    success_url = reverse_lazy("blog:blogrecord_list")
