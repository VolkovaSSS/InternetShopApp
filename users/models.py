from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', blank=True, null=True, help_text='Загрузите аватар')
    phone_number = models.CharField(max_length=25, verbose_name='Телефон', blank=True, null=True, help_text='Введите номер телефона')
    country = models.CharField(max_length=60, verbose_name='Страна', blank=True, null=True, help_text='Введите страну')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def Meta(self):
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

