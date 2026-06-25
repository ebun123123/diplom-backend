
from django.db import models

class KitchenStyle(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название стиля (например, Лофт)")
    description = models.TextField(verbose_name="Краткое описание")
    image_url = models.URLField(max_length=500, verbose_name="Ссылка на изображение")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Стиль кухни"
        verbose_name_plural = "Стили кухонь"