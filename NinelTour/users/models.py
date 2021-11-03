from django.db import models


class User(models.Model):
    GENDERS = [('m', 'man'), ('w', 'women')]

    name = models.CharField(max_length=40, null=False, verbose_name='Имя')
    surname = models.CharField(max_length=40, null=False, verbose_name='Фамилия')
    birthday = models.DateField(null=False, verbose_name='Дата рождения')
    gender = models.CharField(null=False, verbose_name='Пол', max_length=1, choices=GENDERS)
    passport_number = models.CharField(null=False, max_length=6, verbose_name='Номер паспорта')
    email = models.EmailField(null=False, max_length=50, verbose_name='Почта')
    phone = models.CharField(null=True, max_length=12, verbose_name='Телефонный номер')

    def __str__(self):
        return 'Клиент'
