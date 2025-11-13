# news/models.py
from django.db import models


class News(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Текст новости", blank=True)
    video = models.FileField("Видео", upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField("Изображение", upload_to='news/')
    caption = models.CharField("Подпись", max_length=200, blank=True)

    def __str__(self):
        return f"Изображение для {self.news.title}"

    class Meta:
        verbose_name = "Изображение новости"
        verbose_name_plural = "Изображения новостей"