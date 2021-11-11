from django.db import models


class Package(models.Model):
    ROOM_TYPES = [
        ('standard', 'Стандартный'), ('apartment', 'Апартаменты'), ('double', 'Двуместный'),
        ('single', 'Одноместный'), ('triple', 'Трехместный'), ('business', 'Бизнес'), ('family', 'Семейный')
    ]

    MEALS_TYPE = [
        ('AI', 'Все включено'), ('BB', 'Завтраки'), ('HB', 'Полупансион'),
        ('OB', 'Без еды'), ('FB', 'Полный пансион')
    ]

    tour_operator = models.CharField(null=True, max_length=20, verbose_name='Туроператор')
    airline = models.CharField(null=True, max_length=30, verbose_name='Авиакомпания')
    flight_number = models.CharField(null=False, max_length=6, verbose_name='Номер рейса')
    arrival_city = models.CharField(null=False, max_length=20, verbose_name='Город отправки')
    departure_city = models.CharField(null=False, max_length=20, verbose_name='Город назначения')
    departure_country = models.CharField(null=False, max_length=20, verbose_name='Страна назначения')
    hotel_name = models.CharField(null=False, max_length=30, verbose_name='Название отеля')
    room_type = models.CharField(null=True, max_length=10, choices=ROOM_TYPES, verbose_name='Тип комнаты')
    meals_type = models.CharField(null=True, max_length=2, choices=MEALS_TYPE, verbose_name='Тип питания')
    transfer = models.BooleanField(null=False, default=False, verbose_name='Наличие трансфера')
    insurance = models.BooleanField(null=False, default=False, verbose_name='Наличие страховки')

    def __str__(self):
        return f'Туристический пакет №{self.id}'

    class Meta:
        verbose_name_plural = "Туристические пакеты"
        verbose_name = 'Туристический пакет'


