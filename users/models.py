from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", blank=True, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    birthdate = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    gender_choices = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('O', 'Другой'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, null=True, blank=True, verbose_name='Пол')

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
