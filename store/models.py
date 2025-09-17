from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Name")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    currency = models.CharField(max_length=10, default="HUF", verbose_name="Валюта")
    image = models.ImageField(upload_to="products/%Y/%m/%d/", verbose_name="Изображение")
    in_stock = models.BooleanField(default=True, verbose_name="В наличии")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created_at']

    def __str__(self):
        return self.name