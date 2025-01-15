from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True)  # Основной ключ
    name = models.CharField(max_length=100)  # Название телефона
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    image = models.ImageField(upload_to="phones/", blank=True, null=True)  # Картинка
    release_date = models.DateField()  # Дата выпуска
    lte_exists = models.BooleanField(default=False)  # LTE поддержка
    slug = models.SlugField(max_length=100, unique=True, blank=True)  # Слаг

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
