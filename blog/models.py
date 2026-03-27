from django.db import models


class BlogRecord(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="blog/preview_images",
        blank=True,
        null=True,
        verbose_name="Превью",
    )
    is_published = models.BooleanField(verbose_name="Признак публикации")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
