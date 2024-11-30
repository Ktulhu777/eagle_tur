from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    balance = models.DecimalField(
        default=0,
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return f'Username: - {self.username} | E-mail: -{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
