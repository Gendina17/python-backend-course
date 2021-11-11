from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDERS = [('m', 'Мужчина'), ('w', 'Женщина')]

    birthday = models.DateField(null=False, verbose_name='Дата рождения')
    gender = models.CharField(null=False, verbose_name='Пол', max_length=1, choices=GENDERS)
    passport_number = models.CharField(null=False, max_length=6, verbose_name='Номер паспорта', unique=True)
    phone = models.CharField(null=True, max_length=12, verbose_name='Телефонный номер')

    def __str__(self):
        return f'Клиент {self.id} - {self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('show_user', kwargs={'id': self.id})

    class Meta:
        verbose_name_plural = "Клиенты"
        verbose_name = 'Клиент'
