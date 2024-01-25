from email.policy import default
from tabnanny import verbose
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"


class Products(models.Model):
    name        = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug        = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image       = models.ImageField(upload_to="goods_images", blank=True, null=True, verbose_name="Фото"    )
    price       = models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name="Цена")

    class Meta:
        db_table = "product"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
