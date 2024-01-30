from django.db import models
from goods.models import Products

from users.models import User


class Cart(models.Model):
    user              = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Пользователь")
    product           = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name="Продукт")
    quantity          = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name        = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"Корзина{self.user.username} | Товар {self.product.name} | Количество {self.quantity}"
    